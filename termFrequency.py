""""
    File name: termFrequency.py
    Author: Wenxin Fang
    Date created: 11/12/2017
    Python Version: 2.7
"""
from collections import Counter

"""
    Open specific file and sparse document
    Strip out punctuation, split by whitespace, and convert everything to lowercase
    Input: file name
    Output: list of words
"""
def fileopen(filename):
    s = "?.()',!:-;"
    words = []
    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                for i in s:
                    if i == "'":
                        word = word.replace(i, " ").lower().split()[0]
                    word = word.replace(i, "").lower()
                    word = word.replace('"', "").lower()
                words.append(word)
    return words

"""
    Calculate term frequency
    Input: a list of .txt documents, a list of words
    Ouput: top TF and document for each word
"""
def termFrequency(files, words):
    dict = {}

    # save words in documents as dictionery
    for file in files:
        dict[file] = Counter(fileopen("./documents/" + file))

    print "Ouput top TF and top TF document for each word: "
    output_file = open('output.txt', 'w')
    for word in words:
        max = -1.0
        maxFile = ""
        for file in files:
            temp = dict[file][word] / float(sum(dict[file].values()))
            if (max < temp):
                max = temp
                maxFile = file
        output_file.write(word + "    " + str(max) + "   " + maxFile + "\n")
        print word + "    " + str(max) + "   " + maxFile
    output_file.close()

"""
    Build up test case
"""
def main():
    index = 5
    files = []

    # set of words
    words = ['queequeg', 'whale', 'sea']

    # build up set of documents
    for i in range(index):
        files.append("mobydick-chapter" + str(i + 1) + ".txt")

    print "Input documents: "
    for file in files:
        print file,
    print
    print

    termFrequency(files, words)



if __name__ == "__main__":
    main()