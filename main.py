"""
Testing flask web app

"""

from flask import Flask, jsonify
from passlib.hash import pbkdf2_sha256

APP = Flask(__name__)

@APP.route('/oauth/authorize', methods=['GET', 'POST'])
def authorize():
    """ grant token via OAuth2 """
    return jsonify("hello world")
