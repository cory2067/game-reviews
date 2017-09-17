import json
import random
from textblob import TextBlob

# the db has ~20038 entries
class Generator():

    def __init__(self):
        self.db = []
        with open('db.json') as f:
            for line in f:
                self.db.append(json.loads(line))

    def generate(self):
        review_id = random.randint(0, 20037)
        text = self.db[review_id]['reviewText']
        payload = {'review': review_id}
        words = TextBlob(text).tags

        libs = []
        def add(i, w, pos):
            libs.append({
                'id': i,
                'word': w,
                'pos': pos,
            })

        for i, (w, pos) in enumerate(words):
            if random.random() > 0.4:
                continue

            if pos == 'NN':
                add(i, w, 'Noun')
            elif pos == 'NNS':
                add(i, w, 'Plural Noun')
            elif pos == 'JJ':
                add(i, w, 'Adjective')
            elif pos == 'JJR':
                add(i, w, '-er Adjective')
            elif pos == 'JJS':
                add(i, w, '-est Adjective')
            elif pos == 'VBD':
                add(i, w, 'Past Tense Verb')
            elif pos == 'VGB':
                add(i, w, 'Gerund (Verb-ing)')

        payload['words'] = libs
        return payload
