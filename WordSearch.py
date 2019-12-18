#  File: WordSearch.py

#  Description: Finds specified words in a words search from an input file named hidden.txt, 
#  outputs coordinate locations of found words to file named found.txt

#  Student Name: Samuel McKean

#  Student UT EID: slm4699

#  Partner Name: Andrew Dinh

#  Partner UT EID: ad42344

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/14/19

#  Date Last Modified: 9/15/19

# main () calls all functions for WordSearch.py
def main():
    wordSearchDim, wordSearch, numberOfWords, words = file_read()
    foundWords = dict_init(words)
    row_search(wordSearchDim, wordSearch, words, foundWords)
    column_search(wordSearchDim, wordSearch, words, foundWords)
    diag_search(wordSearchDim, wordSearch, words, foundWords)
    file_write(wordSearchDim, foundWords, words)
# file_read() opens the file hidden.txt and returns dimensions of wordsearch as list, the wordsearch it self as a list
# of strings, the number of words to be searched, and the words to be searched as list
def file_read():
    with open('hidden.txt', 'r') as fileContents:
        wordSearchDim = list(map(int, fileContents.readline().split()))
        fileContents.readline()
        wordSearch = []
        for row in range(wordSearchDim[0]):
            wordSearch.append(fileContents.readline().strip().replace(' ', ''))
        fileContents.readline()
        numberOfWords = int(fileContents.readline().strip())
        words = []
        for row in range(numberOfWords):
            words.append(fileContents.readline().strip())
    return wordSearchDim, wordSearch, numberOfWords, words
# dict_init initializes a dictionary containing the words as keys and the words' first characters' coordinates as values
def dict_init(words):
    foundWords = {}
    for word in words:
        foundWords[word] = (0, 0)
    return foundWords
# row_search() searches each row in the wordsearch for the words, forwards and backwards; if the word is found, the word
# and its first character's coordinate is added to the dictionary: foundWords
def row_search(wordSearchDim, wordSearch, words, foundWords):
    for i in range(wordSearchDim[0]):
        for word in words:
            if wordSearch[i].find(word) != -1:
                foundWords[word] = (i+1, wordSearch[i].find(word)+1)
            rev_word = word[::-1]
            if wordSearch[i].find(rev_word) != -1:
                foundWords[word] = (i+1, wordSearch[i].find(rev_word)+len(rev_word))
    return foundWords
# column_search() creates strings from the wordsearch columns and searches for the words, forwards and backwards;
# if the word is found, it is added to the dictionary as described in row_search()
def column_search(wordSearchDim, wordSearch, words, foundWords):
    for j in range(wordSearchDim[1]):
        column = ''
        for i in range(wordSearchDim[0]):
            column += wordSearch[i][j]
        for word in words:
            if column.find(word) != -1:
                foundWords[word] = (column.find(word)+1, j+1)
            rev_word = word[::-1]
            if column.find(rev_word) != -1:
                foundWords[word] = (column.find(rev_word)+len(rev_word), j+1)
    return foundWords
# diag_search() creates strings from the wordsearch diagonals and searches for the words, forwards and backwards;
# same documentation as row_search()
def diag_search(wordSearchDim, wordSearch, words, foundWords):
    # this searches through the lower diagonals that run from top-left to bottom-right
    for x in range(wordSearchDim[0]):
        diag = ''
        i = x
        j = 0
        while 0 <= i < wordSearchDim[0] and 0 <= j < wordSearchDim[1]:
            try:
                diag += wordSearch[i][j]
                j += 1
                i += 1
            except IndexError:
                break
        for word in words:
            if diag.find(word) != -1:
                foundWords[word] = (diag.find(word)+x+1, diag.find(word)+1)
            rev_word = word[::-1]
            if diag.find(rev_word) != -1:
                foundWords[word] = (diag.find(rev_word)+len(rev_word)+x, diag.find(rev_word)+len(rev_word))
    # this searches through the upper diagonals that run from top-left to bottom-right
    for y in range(1, wordSearchDim[1]):
        diag = ''
        i = 0
        j = y
        while 0 <= i < wordSearchDim[0] and 0 <= j < wordSearchDim[1]:
            try:
                diag += wordSearch[i][j]
                j += 1
                i += 1
            except IndexError:
                break
        for word in words:
            if diag.find(word) != -1:
                foundWords[word] = (diag.find(word) + 1, diag.find(word) + y + 1)
            rev_word = word[::-1]
            if diag.find(rev_word) != -1:
                foundWords[word] = (diag.find(rev_word) + len(rev_word), diag.find(rev_word) + len(rev_word) + y)
    # this searches through lower diagonals running from top-right to bottom-left
    for x in range(wordSearchDim[0]):
        diag = ''
        i = x
        j = wordSearchDim[1]-1
        while 0 <= i < wordSearchDim[0] and 0 <= j < wordSearchDim[1]:
            try:
                diag += wordSearch[i][j]
                j -= 1
                i += 1
            except IndexError:
                break
        for word in words:
            if diag.find(word) != -1:
                foundWords[word] = (diag.find(word)+x+1, wordSearchDim[1]-diag.find(word))
            rev_word = word[::-1]
            if diag.find(rev_word) != -1:
                foundWords[word] = (diag.find(rev_word)+len(rev_word)+x, wordSearchDim[1]-diag.find(rev_word)-len(rev_word)+1)
    # this searches through the upper diagonals running from top-right to bottom-left
    for y in range(wordSearchDim[1] - 1):
        diag = ''
        i = 0
        j = y
        while 0 <= i < wordSearchDim[0] and 0 <= j < wordSearchDim[1]:
            try:
                diag += wordSearch[i][j]
                j -= 1
                i += 1
            except IndexError:
                break
        for word in words:
            if diag.find(word) != -1:
                foundWords[word] = (diag.find(word) + 1, y - diag.find(word) + 1)
            rev_word = word[::-1]
            if diag.find(rev_word) != -1:
                foundWords[word] = (diag.find(rev_word) + len(rev_word), y - diag.find(rev_word) - len(rev_word) + 2)
    return foundWords
# file_write() writes the list of words to be searched for, which may be found or not found in the wordsearch, with
# their corresponding coordinates to found.txt; formatted as a table
def file_write(wordSearchDim, foundWords, words):
    longestWordLen = 0
    for word in words:
        if len(word) > longestWordLen:
            longestWordLen = len(word)
    longestDimLen = len(str(wordSearchDim[0]))
    with open('found.txt', 'w') as fileContents:
        for word in words:
            fileContents.write(word.ljust(longestWordLen + 5))
            fileContents.write((str(foundWords[word][0])).rjust(longestDimLen))
            fileContents.write((str(foundWords[word][1])).rjust(longestDimLen + 2))
            fileContents.write('\n')
main()