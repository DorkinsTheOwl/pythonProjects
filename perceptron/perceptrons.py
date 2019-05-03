from random import shuffle
import numpy as np


class Perceptron:
    def __init__(self, numberOfInputs, learningRate=0.1, nEpoch=10):
        self.weights = [0.0 for _ in range(numberOfInputs)]
        self.learningRate = learningRate
        self.nEpoch = nEpoch

    def predict(self, row):
        activation = self.weights[0]
        for i in range(len(row) - 1):
            activation += self.weights[i + 1] * float(row[i])

        return 1 if activation >= 0.0 else 0

    def trainWeights(self, train):
        for epoch in range(self.nEpoch):
            sumError = 0.0
            shuffle(train)
            for row in train:
                prediction = self.predict(row)
                error = row[-1] - prediction
                sumError += error ** 2
                self.weights[0] += self.learningRate * error
                for i in range(len(row) - 1):
                    self.weights[i + 1] += self.learningRate * error * float(row[i])
            print(f'>epoch={epoch}, learningRate={round(self.learningRate, 3)}, error={round(sumError, 3)}')
            if sumError == 0.0:
                break

    def perceptron(self, train, test, testResults):
        print('Running...')

        self.trainWeights(train)

        results = []
        for row in test:
            prediction = self.predict(row)
            results.append(prediction)

        precision = [0, 0]
        for got, wanted in zip(results, testResults):
            wanted = int(wanted)
            if got == wanted:
                precision[0] += 1
                precision[1] += 1
            else:
                precision[1] += 1

        print(f'Precision = {precision[0]}/{precision[1]} - {round(precision[0] / precision[1], 2) * 100}%')


class PerceptronUtilizingNumpy:
    def __init__(self, numberOfInputs, learningRate=0.1, nEpoch=100):
        self.weights = np.zeros(numberOfInputs + 1)
        self.learningRate = learningRate
        self.nEpoch = nEpoch

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation >= 0 else 0

    def trainWeights(self, setOfInputs):
        for epoch in range(self.nEpoch):
            sumError = 0.0
            shuffle(setOfInputs)
            for inputs, expected in setOfInputs:
                prediction = self.predict(inputs)
                error = expected - prediction
                sumError += error ** 2
                self.weights[0] += self.learningRate * error
                self.weights[1:] += self.learningRate * error * inputs
            print(f'>epoch={epoch}, learningRate={self.learningRate}, error={round(sumError, 2)}')
            if sumError <= 10.0:
                break

    # def prepareDataForTrain():
    #     tweetsWithMarks = [tuple(i.strip('\n').split('\t')) for i in open('./trainingSet.txt', encoding='utf8').readlines()]
    #     tweets = [i[1] for i in tweetsWithMarks]
    #     binaryMarks = [int(i[0]) for i in tweetsWithMarks]
    #
    #     for i in range(3):
    #         tweets = cleanText(tweets)
    #
    #     tfidf = TfidfVectorizer(min_df=2, max_df=0.5, stop_words=lvStopWords, ngram_range=(1, 2))
    #     vocab = tfidf.fit(tweets).vocabulary_
    #     with open('vocab.txt', 'w+', encoding='utf8') as f:
    #         f.write(str(vocab))
    #     tweets = tfidf.fit_transform(tweets).toarray()
    #     binaryMarks = np.array(binaryMarks)
    #     print('Adjusting weights')
    #     arrayOfWeights = train(tweets, binaryMarks)
    #     print('Weight adjustment complete')
    #     np.savetxt('./listOfWeights2.txt', arrayOfWeights)

    def perceptron(self, trainTweets, trainResults, testTweets, testResults):
        print('Running...')

        self.trainWeights(list(zip(trainTweets, trainResults)))

        results = []
        for row in testTweets:
            prediction = self.predict(row)
            results.append(prediction)

        precision = [0, 0]
        for got, wanted in zip(results, testResults):
            wanted = int(wanted)
            if got == wanted:
                precision[0] += 1
                precision[1] += 1
            else:
                precision[1] += 1

        print(f'Precision = {precision[0]}/{precision[1]} - {round(precision[0] / precision[1], 2) * 100}%')
