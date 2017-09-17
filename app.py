import json
import random
from textblob import TextBlob
from flask import Flask
from flask import render_template
app = Flask(__name__)

db = []

def add(i, w, pos, libs):
    libs.append({
        'id': i,
        'word': w,
        'pos': pos,
    })

def load_database():
    print("Loading db...")
    with open('db.json') as f:
        for line in f:
            db.append(json.loads(line))

    print("Done.")
    return db

def load_matlib():
    review_id = random.randint(0, len(db)-1)
    text = db[review_id]['reviewText']
    words = TextBlob(text).tags

    payload = {'review': review_id}
    libs = []

    for i, (w, pos) in enumerate(words):
        if random.random() > 0.4:
            continue

        if pos == 'NN':
            add(i, w, 'Noun', libs)
        elif pos == 'NNS':
            add(i, w, 'Plural Noun', libs)
        elif pos == 'JJ':
            add(i, w, 'Adjective', libs)
        elif pos == 'JJR':
            add(i, w, '-er Adjective', libs)
        elif pos == 'JJS':
            add(i, w, '-est Adjective', libs)
        elif pos == 'VBD':
            add(i, w, 'Past Tense Verb', libs)
        elif pos == 'VGB':
            add(i, w, 'Gerund (Verb-ing)', libs)

    payload['words'] = libs

    print(payload)

@app.route("/")
def index(loaded=False):
    try:
        load_matlib()
    except: # db is empty, so the random number generator gails
        load_database()
        load_matlib()
    return render_template('index.html')

@app.route("/result")
def result(result=None):
    return render_template('result.html', result=None)

app.run('127.0.0.1', '5000')