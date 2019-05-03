from random import shuffle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from perceptrons import Perceptron, PerceptronUtilizingNumpy
from utils import *

lvStopWords = ["aiz", "ap", "apakš", "apakšpus", "ar", "arī", "augšpus", "bet", "bez", "bija", "biji", "biju", "bijām", "bijāt", "būs",
               "būsi", "būsiet", "būsim", "būt", "būšu", "caur", "diemžēl", "diezin", "droši", "dēļ", "esam", "esat", "esi", "esmu", "gan",
               "gar", "iekam", "iekams", "iekām", "iekāms", "iekš", "iekšpus", "ik", "ir", "it", "itin", "iz", "ja", "jau", "jeb", "jebšu",
               "jel", "jo", "jā", "ka", "kamēr", "kaut", "kolīdz", "kopš", "kā", "kļuva", "kļuvi", "kļuvu", "kļuvām", "kļuvāt", "kļūs",
               "kļūsi", "kļūsiet", "kļūsim", "kļūst", "kļūstam", "kļūstat", "kļūsti", "kļūstu", "kļūt", "kļūšu", "labad", "lai", "lejpus",
               "līdz", "līdzko", "ne", "nebūt", "nedz", "nekā", "nevis", "nezin", "no", "nu", "nē", "otrpus", "pa", "par", "pat", "pie",
               "pirms", "pret", "priekš", "pār", "pēc", "starp", "tad", "tak", "tapi", "taps", "tapsi", "tapsiet", "tapsim", "tapt",
               "tapāt", "tapšu", "taču", "te", "tiec", "tiek", "tiekam", "tiekat", "tieku", "tik", "tika", "tikai", "tiki", "tikko",
               "tiklab", "tiklīdz", "tiks", "tiksiet", "tiksim", "tikt", "tiku", "tikvien", "tikām", "tikāt", "tikšu", "tomēr", "topat",
               "turpretim", "turpretī", "tā", "tādēļ", "tālab", "tāpēc", "un", "uz", "vai", "var", "varat", "varēja", "varēji", "varēju",
               "varējām", "varējāt", "varēs", "varēsi", "varēsiet", "varēsim", "varēt", "varēšu", "vien", "virs", "virspus", "vis",
               "viņpus", "zem", "ārpus", "šaipus"]

allTweets = [tuple(i.strip('\n').split('\t')) for i in open('./tweets.train', encoding='utf8').readlines()]
binaryTweetsAndMarks = [i for i in allTweets if i[0] == '-1' or i[0] == '1']
binaryTweets = [i[1] for i in binaryTweetsAndMarks]
binaryMarks = [1 if i[0] == '1' else 0 for i in binaryTweetsAndMarks]
setOfTweets = list(zip(binaryMarks, binaryTweets))
splitIndex = int(len(binaryTweets) * 0.9)
shuffle(setOfTweets)
marks, tweets = zip(*setOfTweets)

for _ in range(3):
    cleanText(tweets)

# vocab (custom dict) should be added when train and test are 2 separate sources
# tfidf = TfidfVectorizer(min_df=2, max_df=0.5, stop_words=lvStopWords, vocabulary=vocab, ngram_range=(1, 2))
tfidf = TfidfVectorizer(min_df=2, max_df=0.5, stop_words=lvStopWords, ngram_range=(1, 2))
tweets = tfidf.fit_transform(tweets).toarray()
marks = np.array(marks)

trainTweets, testTweets = np.split(tweets, [splitIndex])
trainMarks, testMarks = np.split(marks, [splitIndex])

# implementation #1
# this perceptron needs test data that has mark as last index of input
# works slow, precision is above 70%
# perceptron1TestTweets = np.insert(trainTweets, len(trainTweets[0]), trainMarks, axis=1)
# perc = Perceptron(len(perceptron1TestTweets[0]))
# perc.perceptron(trainTweets, testTweets, testMarks)

# implementation #2 utilizing numpy
# works fast, precision is above 70%
percWithNumpy = PerceptronUtilizingNumpy(len(trainTweets[0]))
percWithNumpy.perceptron(trainTweets, trainMarks, testTweets, testMarks)
