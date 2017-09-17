import json
import random
from textblob import TextBlob
from server import MMLL
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index(loaded=False):
    return render_template('index.html')

@app.route("/result")
def result(result=None):
    return render_template('result.html', result=None)

madlibML = MMLL()
madlibML.load_database()
app.run('127.0.0.1', '5000')