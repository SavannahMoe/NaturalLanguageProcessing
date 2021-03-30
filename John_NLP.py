from textblob import TextBlob
import nltk

nltk.download("stopwords")

from nltk.corpus import stopwords
from pathlib import Path

from wordcloud import WordCloud
import imageio
import matplotlib as plt
#import pandas as pd 

blob = TextBlob(Path("BookOfJohn.txt").read_text())

stops = stopwords.words("english")
john_stops = ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall']
stops +=john_stops

words = blob.words
noun_items= blob.noun_phrases
#print(blob.noun_phrases)

items = blob.word_counts.items()
items = [item for item in items if item[0] not in stops if item[0] in noun_items]


from operator import itemgetter
from pathlib import Path

ranked_items = sorted(items, key = itemgetter(1), reverse = True)
top15 = ranked_items[:15]
#print(top15)
word_list = []
for x in top15:
   word_list.append(x[0])

items_str = ' '.join([str(x) for x in word_list])

print(items_str)



wordcloud = WordCloud(colormap="viridis", background_color="gray")
wordcloud = wordcloud.generate(items_str)
wordcloud = wordcloud.to_file("JohnWordCloud.png")


