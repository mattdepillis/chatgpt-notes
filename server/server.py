"""

"""
# dependencies
import configparser
from flask import Flask
from flask_pymongo import PyMongo
import os
import sys

# path management
paths, cwd = [ "/utils/" ], os.getcwd()
for path in paths:
  sys.path.append(cwd + "/utils/")

# import files
import app_secrets
import mongo


# configuration variables
config = configparser.RawConfigParser()
config.read(r'./config.ini')
SECTION = 'DEV'
env = config[SECTION]

# setup flask app
app = Flask(__name__)

# mongo
url = mongo.construct_url(env, app_secrets.mpw)

# routes
@app.route('/')
def handler():
  print("app running on port 5000")
  return f"<p>{env['MONGO_URL_FIRST']}</p>"