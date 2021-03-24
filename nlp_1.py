from textblob import TextBlob
'''
text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob)

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


#stemming algorithms work by cutting off the end or the beginning of the word, taking common prefixes and suffixes that can be found in the inflected word
#varieties would be varieti
#studies would be studi

#lemmatization, on the other hand, takes into consideration the morphological analysis of the words
#varieties would be variety
#studies would be study

from textblob import Word

word1 = Word("studies")
word2= Word("varieties")

#print(word1.lemmatize())
#print(word2.lemmatize())


happy = Word('happy')

#print(happy.definitions)

for synset in happy.synsets:
    print(synset)
    for lemma in synset.lemmas():
        print(lemma)
        print(lemma.name())

lemmas = happy.synsets[0].lemmas()
print(lemmas)

for lemma in lemmas[0].antonyms():
    print(lemma.name())
'''


#stock words 
import nltk

#nltk.download('stopwords')
from nltk.corpus import stopwords

stops = stopwords.words("english")
print(stops)

blob = TextBlob("Today is a beautiful day.")

print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]
print(cleanlist)