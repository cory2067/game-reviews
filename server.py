import json
import random
from textblob import TextBlob

# the db has 231780 entries 
db = []

print("Loading db...")
with open('db.json') as f:
    for line in f:
       db.append(json.loads(line))

print("Done.")

text = db[157630]['reviewText']
words = TextBlob(text).tags

for w in words:
    if w[1] in ('NN','NNS','NNP','NNPS','JJ','JJR','JJS','VBD','VBG'):
        print(w)



