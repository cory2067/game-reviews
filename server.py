import json
import random
from textblob import TextBlob

# the db has ~20038 entries
db = []

print("Loading db...")
with open('db.json') as f:
    for line in f:
       db.append(json.loads(line))

print("Done.")

review_id = 16578
# review_id = random.randint(0, 20037)
text = db[review_id]['reviewText']
words = TextBlob(text).tags

payload = {'review': review_id}
libs = []

def add(i, w, pos):
    libs.append({
        'id': i,
        'word': w,
        'pos': pos,
    })

for i,(w,pos) in enumerate(words):
    if random.random() > 0.4:
        continue

    if pos == 'NN':
        add(i,w,'Noun')
    elif pos == 'NNS':
        add(i,w,'Plural Noun')
    elif pos == 'JJ':
        add(i,w,'Adjective')
    elif pos == 'JJR':
        add(i,w,'-er Adjective')
    elif pos == 'JJS':
        add(i,w,'-est Adjective')
    elif pos == 'VBD':
        add(i,w,'Past Tense Verb')
    elif pos == 'VGB':
        add(i,w,'Gerund (Verb-ing)')

payload['words'] = libs

print(payload)
