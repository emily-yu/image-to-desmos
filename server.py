from flask import Flask, request
import urllib.request
import requests
import string
import re
import json
from image_line import execute_zhang_suen
import base64

app = Flask(__name__)

@app.route('/new_image') # returns coords
def new_image():
    file_name = request.args.get("file")
    # if coded_string:
    # 	return execute_zhang_suen(base64.b64decode(coded_string))

    # return execute_zhang_suen('leaf-identification.jpg')
    return execute_zhang_suen(file_name)

if __name__ == '__main__':
        app.run()
