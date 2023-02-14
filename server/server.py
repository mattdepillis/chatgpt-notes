"""
Main entrypoint for the Flask server - a REST API that connects to MongoDB Atlas datastore.
"""
# dependencies
import configparser
from flask import Flask
from flask_pymongo import MongoClient
import os
import sys

# path management
paths, cwd = [ "/utils/" ], os.getcwd()
for path in paths:
  sys.path.append(cwd + "/utils/")

# import files
import app_secrets
import mongodb

# configuration variables
config = configparser.RawConfigParser()
config.read(r'./config.ini')
env = config["DEV"]

# setup flask app
app = Flask(__name__)

# mongo
url = mongodb.construct_url(env, app_secrets.mpw)
mongo = MongoClient(url)
table = mongo[env["DB"]]["comments"]

# routes
@app.route('/')
def handler():
  print("app running on port 5000")
  comments = table.find_one({ "name" : "John Bishop" })
  return f"<p>{comments}</p>"