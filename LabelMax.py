### Main Entry Point

# Import and prep dotenv
import os
import os.path
##from dotenv import load_dotenv
#import time
import label_app.scripts.gmail_api as gmail_api_script
import label_app.utils.local_database as db_script
# import label_app.util.util_manager as util_script

## Load environment variables from the .env file
#load_dotenv()

## Access the environment variables in your code
#api_key = os.getenv('GMAIL_API_KEY')
##debug = os.getenv('DEBUG') == 'True'

# Run the gmail_api_script main function
gmail_api_script.main()
print("Gmail API Script Complete")
# Run the db_script main function
db_script.main()
print("Database Script Complete")
print("LabelMax Complete")


### Import the necessary libraries and any associated or required; google-api-python-client, numpy, pandas, nltk, scikit-learn, gensim, tensorflow, flask.
##import os
##import sys
##import json
##import time
##import datetime
##import numpy as np
##import pandas as pd
##import nltk
##import gensim
##import tensorflow as tf
### pull out important modules from imported libraries
##from flask import flask, request, jsonify
##from flask_cors import cors
### google-api-python-client  import
##from googleapiclient.discovery import build
##from googleapiclient.errors import httperror
##from oauth2client.tools import argparser
### nltk import
##from nltk.corpus import stopwords
##from nltk.stem import wordnetlemmatizer
### scikit-learn import
##from sklearn.feature_extraction.text import tfidfvectorizer
##from sklearn.metrics.pairwise import cosine_similarity
### gensim import
##from gensim.models import word2vec
### tensorflow import
##from tensorflow.keras.preprocessing.text import tokenizer
##from tensorflow.keras.preprocessing.sequence import pad_sequences
### flask import
##from flask import flask, request, jsonify
##from flask_cors import cors
### import a dotenv type library to hide the api key
##from dotenv import load_dotenv
### path: labelmax.py
### define the flask app
##app = flask(__name__)
##cors(app)
### path: labelmax.py

### define the global variables.