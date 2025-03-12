#html-to-freq.py

# original lesson: https://programminghistorian.org/en/lessons/counting-frequencies

# We've added json to the list of imports — you don't need to install anything,
# json is part of the Python standard library.
import urllib.request, urllib.error, urllib.parse, json, obo

# Notice that instead of requesting the HTML directly, we're now
# making a request to the backend API — meaning a server that returns
# data directly.
url = 'https://www.dhi.ac.uk/api/data/oldbailey_record_single?idkey=t17800628-33'

# We can make the request as before
response = urllib.request.urlopen(url)

# Similarly, we can parse the body as before
body = response.read().decode('UTF-8')

# However, unlike how this lesson used to work, we need to parse
# body — which is a string — as JSON, which is represented
# in Python as a dictionary. To do this, we use the json.loads()
# function
record = json.loads(body)

# The record is now a Python dictionary of dictionaries —
# remember how these work? You should feel free to explore
# the keys and values that are available, but the line
# below will return the basic HTML that the original
# script expected.
html = record['hits']['hits'][0]['_source']['html']

# With the HTML now in hand, we can continue to run
# the original word frequencies script as usual.
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))