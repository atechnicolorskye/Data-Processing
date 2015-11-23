"""
Word2Vec.py

Description
-----------
Uses the Python Word2Vec implementation to generate word vectors.

Word2Vec('ptb.txt', size=200, workers=2, min_count=1)

size sets the length of the output feature vector
workers sets the number of cores used
min_count sets the minimum times a word must appear before it is added to the list of the words to be vectorized

Please refer to http://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.Word2Vec for more information

"""

""
import gensim

def Word2Vec(filename, size=50, workers=1, min_count=1):

    with open('New_Sentences_Interest.txt', 'r') as F:
        Sentences = F.readlines()

    Input = []

    for sentence in Sentences:
        Input.append(sentence.split())

    model = gensim.models.Word2Vec(Input, size=size, workers=workers, min_count=min_count)

    print model

    New_File = 'Word2Vec_' + str(size) + '_' + filename

    F = open(New_File, "w")

    for x in (range(len(model.index2word))):
        F.write(str(model.index2word[x]) + ' ' + str(model[model.index2word[x]]) + ' ' + '\n')

    F.close

    return model

Word2Vec('New_Sentences_Interest.txt', size=50, workers=2, min_count=1)