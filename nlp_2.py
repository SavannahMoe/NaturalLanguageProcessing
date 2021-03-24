from textblob import TextBlob
import nltk

nltk.download("stopwords")

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd 

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())
'''
print(blob.word_counts["juliet"])
print(blob.word_counts['romeo'])
print(blob.word_counts['thou'])
print(blob.words.count("joy"))
print(blob.noun_phrases.count("lady capulet"))
'''

stops = stopwords.words("english")
more_stops = ['thee', 'thy', 'thou']
stops += more_stops

#print(stops)

items = blob.word_counts.items()

#use a list comprehension to eliminate any tuples containing stop words: 
items = [item for item in items if item[0] not in stops]
#print(items[:10])

#to determine the top 20 words sort the tuples in items in descending order by element 1 
#we can use built-in funciton sorted with a key

from operator import itemgetter

#sorted_items = sorted(items)
#print(sorted_items[:10])

sorted_items = sorted(items, key=itemgetter(1), reverse = True)
print(sorted_items[:10])

top20 = sorted_items[:20]
print(top20)

df = pd.DataFrame (top20, columns = ['word','count'])
print(df)

import matplotlib.pyplot as plt

df.plot.bar(x = "word", y = "count",rot=0, legend=False, color=["y", "c","m","b","g","r"])
plt.gcf().tight_layout()
plt.show()