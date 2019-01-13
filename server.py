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
import base64

app = Flask(__name__)

@app.route("/")
def hello():
    return "hey its me"

@app.route('/new_image') # returns coords
def new_image():
    # http://30e415d8.ngrok.io/sendverificationcode?countrycode=1&number=6505754922
    file_name = request.args.get("file")
    # if coded_string:
    # 	return execute_zhang_suen(base64.b64decode(coded_string))

    # return execute_zhang_suen('leaf-identification.jpg')
    return execute_zhang_suen(file_name)

if __name__ == '__main__':
        app.run()
