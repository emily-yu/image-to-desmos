from flask import Flask, request
# from twilio.rest import Client
import urllib.request
# from bottle import route, run, template, static_file, get, post, request
import requests
# from secret import getSID, getAuth, getAuthy
import string
import re
import json
from image_line import execute_zhang_suen

app = Flask(__name__)

@app.route("/")
def hello():
    return "hey its me"

@app.route('/new_image') # returns coords
def new_image():
    # http://30e415d8.ngrok.io/sendverificationcode?countrycode=1&number=6505754922
    base64 = request.args.get("base64")
    
    return execute_zhang_suen()

if __name__ == '__main__':
        app.run()
