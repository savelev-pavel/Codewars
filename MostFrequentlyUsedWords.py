'''A function that, given a string of text (possibly with punctuation and line-breaks), returns
 an array of the top-3 most occurring words, in descending order of the number of occurrences.'''

def top_3_words(text):
    wordCharsList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '\'']
    separatorList, wordList = [], []
    for char in text:
        if char not in separatorList and char not in wordCharsList:
            separatorList.append(char)
    firstindex = 0
    secondindex = 0

# Попробовать через сплит и separator поэтапно разбить и стрипнуть

    for index, char in enumerate(text):
        if char in separatorList:
            secondindex = index
            for separator in separatorList:
                word = text[firstindex:secondindex].strip(separator)
            if word != '':
                wordList.append(word)
        firstindex = index

    print(wordCharsList)
    print(separatorList)
    print(wordList)

top_3_words('huy huy huy one two, three\\>.<,')