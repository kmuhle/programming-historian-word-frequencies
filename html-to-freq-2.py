#html-to-freq-2.py

import urllib.request, urllib.error, urllib.parse, json, obo

url = 'https://www.dhi.ac.uk/api/data/oldbailey_record_single?idkey=t17800628-33'

response = urllib.request.urlopen(url)
body = response.read().decode('UTF-8')
record = json.loads(body)
html = record['hits']['hits'][0]['_source']['html']
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))

# Implementing the word counts using the Counter object
from collections import Counter

full_counts = Counter(fullwordlist)

counts = Counter(wordlist)

for word, count in counts.items(): 
    print(f'{word}:{count}')
