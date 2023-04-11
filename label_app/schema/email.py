import os.path

# Definte global variables to hold results from API calls and for testing. Need a place to store the following variables:
#   - List of emails
#   - List of email subjects
#   - List of email bodies
#   - List of email senders
#   - List of email recipients
#   - List of email dates
#   - List of labels
#   - List of label names
#   - List of label ids
#   - Credential validation status
#   - Service validation status
# A class to hold the above variables and methods to access them.

class GmailAPI:
    def __init__(self):
            self.emails = []
            self.email_subjects = []
            self.email_bodies = []
            self.email_senders = []
            self.email_recipients = []
            self.email_dates = []
            self.labels = []
            self.label_names = []
            self.label_ids = []
            #self.credential_validation = False
            #self.service_validation = False
    def get_emails(self):
        return self.emails
    def get_email_subjects(self):
        return self.email_subjects
    def get_email_bodies(self):
        return self.email_bodies
    def get_email_senders(self):
        return self.email_senders
    def get_email_recipients(self):
        return self.email_recipients
    def get_email_dates(self):
        return self.email_dates
    def get_labels(self):
        return self.labels
    def get_label_names(self):
        return self.label_names
    def get_label_ids(self):
        return self.label_ids
    #def get_credential_validation(self):
    #    return self.credential_validation
    #def get_service_validation(self):
    #    return self.service_validation
    def set_emails(self, emails):
        self.emails = emails
    def set_email_subjects(self, email_subjects):
        self.email_subjects = email_subjects
    def set_email_bodies(self, email_bodies):
        self.email_bodies = email_bodies
    def set_email_senders(self, email_senders):
        self.email_senders = email_senders
    def set_email_recipients(self, email_recipients):
        self.email_recipients = email_recipients
    def set_email_dates(self, email_dates):
        self.email_dates = email_dates
    def set_labels(self, labels):
        self.labels = labels
    def set_label_names(self, label_names):
        self.label_names = label_names
    def set_label_ids(self, label_ids):
        self.label_ids = label_ids
    #def set_credential_validation(self, credential_validation):
    #    self.credential_validation = credential_validation
    #def set_service_validation(self, service_validation):
    #    self.service_validation = service_validation