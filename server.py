import json
import random
from textblob import TextBlob

# the db has ~20038 entries
class MMLL():

    def __init__(self):
        self.db = []
        self.libs = []
        self.payload = {'review': 0}

    def add(self, i, w, pos):
        self.libs.append({
            'id': i,
            'word': w,
            'pos': pos,
        })

    def load_database(self):
        print("Loading db...")
        with open('db.json') as f:
            for line in f:
                self.db.append(json.loads(line))

        print("Done.")

    def load_MMLL(self):
        if self.libs: # if there were previous libs
            self.libs = []

        review_id = random.randint(0, 20037)
        text = self.db[review_id]['reviewText']
        words = TextBlob(text).tags

        for i, (w, pos) in enumerate(words):
            if random.random() > 0.4:
                continue

            if pos == 'NN':
                self.add(i, w, 'Noun')
            elif pos == 'NNS':
                self.add(i, w, 'Plural Noun')
            elif pos == 'JJ':
                self.add(i, w, 'Adjective')
            elif pos == 'JJR':
                self.add(i, w, '-er Adjective')
            elif pos == 'JJS':
                self.add(i, w, '-est Adjective')
            elif pos == 'VBD':
                self.add(i, w, 'Past Tense Verb')
            elif pos == 'VGB':
                self.add(i, w, 'Gerund (Verb-ing)')

        self.payload['words'] = self.libs

        print(self.payload)

