"""
Main entrypoint for the Flask server - a REST API that connects to MongoDB Atlas datastore.
"""
# dependencies
import configparser
from flask import Flask
from flask_cors import CORS
from flask_pymongo import MongoClient
from bson import json_util
import json
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
# CORS(app, resources={r"/*": { "origins": "*" }})
CORS(app)
app.config["CORS_ORIGINS"] = ["*", "http://localhost:3000"]

# mongo
url = mongodb.construct_url(env, app_secrets.mpw)
mongo = MongoClient(url)
table = mongo[env["DB"]]["comments"]

# routes
@app.route('/t')
def handler():
  print("app running on port 5000")
  comments = table.find_one({ "name" : "John Bishop" })
  c = json_util.dumps(comments)
  print('got c', c)
  return c