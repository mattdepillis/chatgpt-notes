# What is chatgpt-notes?

# Features

# Running Locally

## DB

## Flask Server
- this project was written using a virtual python enviroment using python3.7.2.
- to run the server locally, you should create a virtual environment on your machine using python3.7. you can achieve this using [venv](https://docs.python.org/3/library/venv.html) or [conda](https://docs.conda.io/en/latest/). make sure to install Flask into your venv with ```pip3 install Flask```.
- your IDE needs access to your venv in order to recognize and use packages such as Flask. if using VSCode, for example, ensure you enable the "Status Bar" view and select your new interpreter. if you have Flask installed properly, for example, ```from flask import Flask``` in ```server.py ``` should work as expected.

- TODO: explaining backend structure
- TODO: spinning up the server
  - in root: ```export FLASK_APP=./server/flaskr/server.py```
  - run:
    - debug mode: ```flask --debug run```
    - regular: ```flask run```

## React UI