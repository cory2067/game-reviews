import json
import random
from textblob import TextBlob
from generator import Generator
from flask import Flask, request
from flask import render_template, session

app = Flask(__name__)
app.secret_key = 'shh its a secrets'
gen = Generator()

@app.route("/")
def index(loaded=False):
    session['data'] = None
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    result = json.loads(request.form['data'])
    return render_template('result.html', result=gen.make_result(result))

@app.route("/game")
def show_entry():
    return render_template('game.html', data=json.dumps(gen.generate()))



app.run('127.0.0.1', '5000')
