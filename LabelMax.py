#import the necessary libraries and any associated or required; google-api-python-client, numpy, pandas, nltk, scikit-learn, gensim, tensorflow, flask.
import os
import sys
import json
import time
import datetime
import numpy as np
import pandas as pd
import nltk
import gensim
import tensorflow as tf
# pull out important modules from imported libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
# google-api-python-client  import
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
# nltk import
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# scikit-learn import
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# gensim import
from gensim.models import Word2Vec
# tensorflow import
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# flask import
from flask import Flask, request, jsonify
from flask_cors import CORS
# import a dotenv type library to hide the API key
from dotenv import load_dotenv
# Path: LabelMax.py
# Define the flask app
app = Flask(__name__)
CORS(app)
# Path: LabelMax.py

# Define the global variables.