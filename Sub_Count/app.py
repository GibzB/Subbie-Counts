from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from flask import jsonify
from flask import make_response
from flask import send_file
from flask import send_from_directory
from flask import abort
from flask import Response
from flask import stream_with_context
from flask import g

# Create a webpage
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


