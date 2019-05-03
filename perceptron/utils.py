def cleanText(sentences):
    wordsToRemove = ('http', '0', '00', '@', '.')
    modifiedSentences = []
    for sentence in sentences:
        listOfWords = sentence.strip().split()
        for word in listOfWords:
            if word.startswith(wordsToRemove):
                listOfWords.remove(word)

        modifiedSentences.append(' '.join(listOfWords))

    return modifiedSentences
