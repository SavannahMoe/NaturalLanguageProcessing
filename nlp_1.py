from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob)
'''
print(blob.sentences) #get sentences
#output [Sentence("Today is a beautiful day."), Sentence("Tomorrow looks like bad weather.")]
#each of those are sentence objects
print(blob.words)       #gets words 

print(blob.tags)

print(blob.noun_phrases)

#sentiment analysis
#output polarity(-1=negative|1=positive) and subjectivity (-1\1 objective)
print(blob.sentiment)
#separating them and rounding to 3 decimal places (mut round individually because .sentiment is an object and .sentiment.polority is a value)
print(round(blob.sentiment.polarity,3))
print(round(blob.sentiment.subjectivity,3))
'''
'''
sentences = blob.sentences
for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity,3))


##DIFFERENT ANALYZER
from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob(text, analyzer = NaiveBayesAnalyzer())
print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

blob.detect_language()  ###detect the language of the text
#return would be 'en' indicating it is in english
spanish = blob.translate(to='es')
print(spanish)

'''

from textblob import Word

index = Word('index')
print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())

animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

##SPELL CHECK AND CORRECTION

word = Word('theyr')
print(word.spellcheck())
#output [('they', 0.5713042216741622), ('their', 0.42869577832583783)] (options and confidence level that that is the word desired)

corrected_word = word.correct()

sentence = TextBlob("Ths sentense has missplled wrds")
corrected_sentence = sentence.correct()

print(corrected_word)
print(corrected_sentence)
