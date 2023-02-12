"""

"""
# dependencies
from flask import Flask
from flask_pymongo import PyMongo
import configparser
import os

# configuration variables
config = configparser.RawConfigParser()
config.read(r'./config.ini')
SECTION = 'DEV'
env = config[SECTION]

# setup flask app
app = Flask(__name__)

# routes
@app.route('/')
def handler():
  print("app running on port 5000")
  return f"<p>{env['MONGO_URL']}</p>"