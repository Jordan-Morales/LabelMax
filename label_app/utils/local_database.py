# Local Database utility tool.
from mimetypes import init
import sqlite3
import os

# Define the database file name and path.
db_file = '.\label_app\db\local_database.db'

# Define connection to the database.
conn = sqlite3.connect(db_file)
print('Connected to the database.')

# Define the cursor.
c = conn.cursor()
print('Cursor created.')

# A function to reconnect the database.
def reconnect():
    #global conn
    #global c
# Define connection to the database.
    conn = sqlite3.connect(db_file)
    # Define the cursor.
    c = conn.cursor()
    print('Reconnected to the database.')

# Define a small tpying system to associate table names with their respective id columns for use in the insert_data function, and other functions.
table_names = {
'emails': 'email_id',
'labels': 'label_id',
'senders': 'sender_id',
'auth': 'auth_id'
}

# Define the schema for the data to be inserted using the insert_data into a table based on the table name and using the table_names dictionary.
data_schema = {
'emails': 'email_id, email_subject, email_label, email_sender',
'labels': 'label_id, label_name',
'senders': 'sender_id, sender_name',
'auth': 'auth_id, auth_token'
}

# Define a function to create the database.
def create_database():
    print('Creating database...')
    # Create the database file if it does not exist.
    if not os.path.exists(db_file):
        # Create the database file.
        open(f'.\label_app\db\{db_file}', 'w').close()
        # Create the database tables.
        create_tables()
    else:
        # Create the database tables.
        create_tables()


## Define a function to create the database tables.
def create_tables():
    print('Creating database tables...')
    # Create the first table for emails if it does not exist, and define the columns: email_id, email_subject, email_label, email_sender.
    c.execute('''CREATE TABLE IF NOT EXISTS emails (email_id INTEGER PRIMARY KEY, email_subject TEXT, email_label TEXT, email_sender TEXT)''')
    # Create the second table for labels if it does not exist, and define the columns: label_id, label_name.
    c.execute('''CREATE TABLE IF NOT EXISTS labels (label_id INTEGER PRIMARY KEY, label_name TEXT)''')
    # Create the third table for senders if it does not exist, and define the columns: sender_id, sender_name.
    c.execute('''CREATE TABLE IF NOT EXISTS senders (sender_id INTEGER PRIMARY KEY, sender_name TEXT)''')
    # Create one more table to hole authorization information if it does not exist, and define the columns: auth_id, auth_token.
    c.execute('''CREATE TABLE IF NOT EXISTS auth (auth_id INTEGER PRIMARY KEY, auth_token TEXT)''')
    # Commit the changes to the database.
    conn.commit()
    # Close the connection to the database.
    conn.close()

# Define a function to insert data into a table in an optimized method used when pulling a large amount of data from the Gmail API used the data_schema dictionary.
def insert_data(table_name, data):
    reconnect()
    print('Inserting data into the database...')
    # Define the query to insert data into the table.
    query = '''INSERT INTO {} ({}) VALUES ({})'''.format(table_name, data_schema[table_name], ','.join('?' * len(data_schema[table_name].split(','))))
    # Execute the query.
    c.executemany(query, data)
    # Commit the changes to the database.
    conn.commit()
    # Close the connection to the database.
    conn.close()

# Function to load data from the database, each table seperately.
def load_data(table_name):
    reconnect()
    print('Loading data from the database...')
    # Define the query to load data from the database.
    query = '''SELECT * FROM {}'''.format(table_name)
    # Execute the query.
    c.execute(query)
    # Fetch the data from the database.
    data = c.fetchall()
    # Close the connection to the database.
    conn.close()
    # Return the data.
    return data

# Define a class to house all of the functions to update data in the database.
class UpdateData:
    # Multiple Functions to update data in each table in the database.
    # Define a function to update data in the emails table.
    def update_email_data(email_id, email_subject, email_label, email_sender):
        reconnect()
        # Define the query to update data in the emails table.
        query = '''UPDATE emails SET email_subject = ?, email_label = ?, email_sender = ? WHERE email_id = ?'''
        # Execute the query.
        c.execute(query, (email_subject, email_label, email_sender, email_id))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Define a function to update data in the labels table.
    def update_label_data(label_id, label_name):
        reconnect()
        # Define the query to update data in the labels table.
        query = '''UPDATE labels SET label_name = ? WHERE label_id = ?'''
        # Execute the query.
        c.execute(query, (label_name, label_id))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Define a function to update data in the senders table.
    def update_sender_data(sender_id, sender_name):
        reconnect()
        # Define the query to update data in the senders table.
        query = '''UPDATE senders SET sender_name = ? WHERE sender_id = ?'''
        # Execute the query.
        c.execute(query, (sender_name, sender_id))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Define a function to update data in the auth table.
    def update_auth_data(auth_id, auth_token):
        reconnect()
        # Define the query to update data in the auth table.
        query = '''UPDATE auth SET auth_token = ? WHERE auth_id = ?'''
        # Execute the query.
        c.execute(query, (auth_token, auth_id))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()


# Define a class to house all of the functions to delete data in the database.
class DeleteData:
    # Multiple Functions to delete data in each table in the database.
    # Function to delete data from the emails table.
    def delete_email_data(email_id):
        reconnect()
        # Define the query to delete data from the emails table.
        query = '''DELETE FROM emails WHERE email_id = ?'''
        # Execute the query.
        c.execute(query, (email_id,))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Function to delete data from the labels table.
    def delete_label_data(label_id):
        reconnect()
        # Define the query to delete data from the labels table.
        query = '''DELETE FROM labels WHERE label_id = ?'''
        # Execute the query.
        c.execute(query, (label_id,))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Function to delete data from the senders table.
    def delete_sender_data(sender_id):
        reconnect()
        # Define the query to delete data from the senders table.
        query = '''DELETE FROM senders WHERE sender_id = ?'''
        # Execute the query.
        c.execute(query, (sender_id,))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Function to delete data from the auth table.
    def delete_auth_data(auth_id):
        reconnect()
        # Define the query to delete data from the auth table.
        query = '''DELETE FROM auth WHERE auth_id = ?'''
        # Execute the query.
        c.execute(query, (auth_id,))
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Function to delete all data from the a table in the database.
    def delete_table_data(table_name):
        reconnect()
        # Define the query to delete all data from the database.
        query = '''DELETE FROM {}'''.format(table_name)
        # Execute the query.
        c.execute(query)
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()
    # Function to delete the database.
    def delete_database():
        reconnect()
        # Define the query to delete the database.
        query = '''DROP DATABASE {}'''.format(db_file)
        # Execute the query.
        c.execute(query)
        # Commit the changes to the database.
        conn.commit()
        # Close the connection to the database.
        conn.close()

# Function to check if the database exists.
def check_database():
# Check if the database exists.
    if os.path.isfile(db_file):
        # If it exists, return True.
        return True
    else:
        # If it does not exist, return False.
        return False

# Function to check if the database contains any tables, and if it does, if they are empty.
def check_database_empty():
# Check if the database contains any tables.
    if len(c.execute('''SELECT name FROM sqlite_master WHERE type='table' ''').fetchall()) == 0:
        # If it does not, return True.
        return True
    else:
        # If it does, check if the tables are empty.
        if len(c.execute('''SELECT * FROM emails''').fetchall()) == 0:
            # If they are, return True.
            return True
        else:
            # If they are not, return False.
            return False


# Initialized and validate the database.
def check_and_init_database():
# Check if the database exists.
    if check_database() == True:
        print('Database exists.')
        # If it does, check if the database is empty.
        if check_database_empty() == True:
            print('Database is empty.')
            # If it is, create the tables in the database.
            create_tables()
            print('Tables created.')
        else:
            print('Database is not empty.')
            print('Nothing to do.')
            # If it is not, do nothing.
            pass
    else:
        print('Database does not exist.')
        # If the database does not exist, create the database.
        create_database()
        print('Database created.')
        # Create the tables in the database.
        create_tables()
        print('Tables created.')




### Main Function
def main():
    print("local_database.py is running")
    # Check and initialize the database.
    check_and_init_database()