"""
ProcessInput.py

Description
-----------
This file reads an input file containing words and their associated vectors. The input format is 'Word [Vector]'. 
The words and their vectors are stored in an empty dictionary with words being keys and vectors value. With the 
methods included in this file, the input can be processed in various ways. There is some minor overlaps with this
file and Extract_Compare.py

However, due to the long time away from the code, I'm not really sure what the code does apart from it being able
to compute the distance of word vectors divided by one and another, the Norm_1 distance and the absolute
distance.  
"""

import re
import numpy as np
# import matplotlib.pyplot as plt

from scipy.spatial.distance import euclidean, cosine

# from Extract_Clusters import Extract_Clusters
# from Extract_Compare import Compare_All_Short_1

def ProcessInput(filename):
    # Create an empty dictionary
    W_V = {}

    # Read file
    F = open(filename, "r")
    Input = F.readlines()
    # print Input
    F.close

    for x in Input:
        y = x.split()
        # print y
        try:
            y[1] = re.sub('\[', '', y[1])
            y[-1] = re.sub('\]', '', y[-1])
            # print y
            z = map(float, y[1:])
            W_V[y[0]] = np.array(z)
        except IndexError:
            print y

    # len(W_V)
    # print W_V
    # print 'ProcessInput Complete!'

    return W_V


def CompareInput(filename_1, filename_2):
    # Create an empty dictionary
    X = []
    Y = []

    # Read file
    F = open(filename_1, "r")
    X_ = F.readlines()
    # print Input
    F.close

    for x in X_:
        x_ = x.split()
        x_[1] = re.sub('\[', '', x_[1])
        x_[-1] = re.sub('\]', '', x_[-1])
        X.append(x_)

    # Read file
    F = open(filename_2, "r")
    Y_ = F.readlines()
    # print Input
    F.close

    for y in Y_:
        y_ = y.split()
        y_[1] = re.sub('\[', '', y_[1])
        y_[-1] = re.sub('\]', '', y_[-1])
        Y.append(y_)

    X_Len = len(X)

    Compare_Sum = 0

    for x in X:
        if x in Y:
            Compare_Sum += 1

    print Compare_Sum
    print X_Len


def Extract_Words_Interest(filename_1, filename_2, k):

    Words_Interest_ = ProcessInput(filename_1)
    Words_Interest = Words_Interest_.keys()

    # print len(Words_Interest)
    # Words_Interest = ['woode','biennials']

    with open(filename_2, 'r') as F:
        Input = F.readlines()

    with open('Words_Interest_Vectors_' + str(K) + '.txt', 'w') as F:

        for line in Input:
            line_ = line.split()
            for word in Words_Interest:
                if word == line_[0][2:-2]:
                    F.write(str(line))
                else:
                    pass

    print 'Extraction Complete!'


def Extract_Process_Words_Interest(filename_1, filename_2, filename_3, z):

    Words_Interest_ = ProcessInput(filename_1)
    Words_Interest = Words_Interest_.keys()

    Missing_Words_Interest = []

    # print len(Words_Interest)

    Words = ProcessInput(filename_2)

    Words_Interest_Vectors = {}

    for word in Words_Interest:
        try:
            Words_Interest_Vectors[word] = Words[word]
        except KeyError:
            # print 'Missing: ' + word
            Missing_Words_Interest.append(word)

    for word in Missing_Words_Interest:
        Words_Interest.remove(word)

    # for word in ['?', 'alabama', 'density', 'traverses']:
    #     if word not in Words_Interest_Vectors.keys():
    #         Words_Interest_Vectors[word] = Words[word]

    print len(Words_Interest_Vectors.keys())

    with open('Extracted_GloVe_300D_' + filename_2[6:-9] + '.txt', 'w') as I: #filename_2[9:-4] filename_2[18:-4]

        for word in Missing_Words_Interest:
            I.write('Missing: ' + str(word) + '\n')

        for word in Words_Interest:
            I.write(str(word) + ' ' + str(Words_Interest_Vectors[word]) + '\n')

    # Words_Interest_Vectors = []

    # for word in Words_Interest:
    #     Words_Interest_Vectors.append([word, Words[word]])

    # Words_Interest_Vectors = {}

    # for word in Words_Interest:
    #     Words_Interest_Vectors[word] = Words[word]

    # print Words_Interest_Vectors

    # Clusters = Extract_Clusters(filename_3)

    # print Clusters

    # Compare_All_Short_1(Words_Interest_Vectors)
    '''
    Euclidean_Distances = {}

    Normal_Distances = {}

    with open('Word_Vectors_Divided_' + filename_3[16:-4] + '.txt', 'w') as C:

        for Z in Words_Interest_Vectors:
            Euclidean_Distances_ = [euclidean(Z[1], Centroid) for Centroid in Clusters]
            Euclidean_Distances[Z[0]] = np.absolute(np.array(Euclidean_Distances_))

        # print Euclidean_Distances

        for word_1 in Words_Interest:
            Z = []
            for word_2 in Words_Interest:
                # print word_1, word_2
                z = np.divide(Euclidean_Distances[word_1], Euclidean_Distances[word_2])
                Z.append(sum(z))

            X = [x / sum(Z) for x in Z]
            Normal_Distances[word_1] = X #[x / min(X) for x in X]
            C.write(str(word_1) + ' ' + str(Normal_Distances[word_1]) + '\n')

    # Normal_Euclidean_Distances = {}

    # with open('Word_Vectors_Norm_1' + filename_3[16:-4] + '.txt', 'w') as C:

    #     for Z in Words_Interest_Vectors:
    #         # Euclidean_Distances_ = [euclidean(Z[1], Centroid) for Centroid in Clusters]
    #         Euclidean_Distances_ = [np.linalg.norm((Z[1] - Centroid), ord=1) for Centroid in Clusters]
    #         # Sum_ = sum(Euclidean_Distances_)
    #         # C.write(str(Sum_) + '\n')
    #         # Euclidean_Distances = [Sum_ - Euclidean_Distance for Euclidean_Distance in Euclidean_Distances_]
    #         # Sum = sum(Euclidean_Distances)
    #         X = [x / sum(Euclidean_Distances_) for x in Euclidean_Distances_]
    #         Normal_Euclidean_Distances[Z[0]] = X
    #         C.write(str(Z[0]) + ' ' + str(Normal_Euclidean_Distances[Z[0]]) + '\n')

    # Added_Distances = {}

    # with open('Word_Vectors_Added_Absolute_' + filename_3[16:-4] + '.txt', 'w') as C:

    #     for Z in Words_Interest_Vectors:
    #         Distances_ = [(Z[1] - Centroid) for Centroid in Clusters]
    #         N = range(len(Distances_))
    #         N.pop(0)
    #         Added_Distances_ = Distances_[0]

    #         for y in N:
    #             Added_Distances_ += Distances_[y]
    #         # Euclidean_Distances_ = [np.linalg.norm((Z[1] - Centroid), ord=1) for Centroid in Clusters]
    #         # Sum_ = sum(Euclidean_Distances_)
    #         # C.write(str(Sum_) + '\n')
    #         # Euclidean_Distances = [Sum_ - Euclidean_Distance for Euclidean_Distance in Euclidean_Distances_]
    #         # Sum = sum(Euclidean_Distances)
    #         X = [x / sum(Added_Distances_) for x in Added_Distances_]
    #         Added_Distances[Z[0]] = [abs(x) for x in X]

    #         # [abs(x) / abs(min(X, key=abs)) for x in X]
    #         C.write(str(Z[0]) + ' ' + str(Added_Distances[Z[0]]) + '\n')


    # Euclidean = []

    # Cosine = []

    # for Z in Words_Interest_Vectors:
    #     Euclidean_Distances_ = [euclidean(Z[1], Centroid) for Centroid in Clusters]
    #     Sum_ = sum(Euclidean_Distances_)
    #     Euclidean.append(Sum_)
    #     Cosine_Distances_ = [cosine(Z[1], Centroid) for Centroid in Clusters]
    #     Sum_ = sum(Cosine_Distances_)
    #     Cosine.append(Sum_)

    # X = range(len(Euclidean))
    '''
    print 'Extraction and processing completed for K = ' + filename_3[16:-4]

    # plt.scatter(X, Euclidean, c='g', marker='o', label='Euclidean')
    # plt.scatter(X, Cosine, c='r', marker='s', label='Cosine')
    # plt.legend()
    # plt.autoscale()
    # plt.show()


def Extract_Compare(filename, word_1, word_2):

    with open(filename, 'r') as F:
        Input = F.readlines()

    for line in Input:
        line_ = line.split()
        if word_1 == line_[0][2:-2]:
            word_1_ = line
        elif word_2 == line_[0][2:-2]:
            word_2_ = line

    Word_Vectors = [word_1_, word_2_]

    for x in range(len(Word_Vectors)):
        y_ = Word_Vectors[x].split(',')
        # print y_
        y_[1] = re.sub('\[', '', y_[1])
        y_[-1] = re.sub('\] \]', '', y_[-1])
        y = y_[1:]
        z = map(float, y)
        Word_Vectors[x] = z

    Euclidean = euclidean(Word_Vectors[0], Word_Vectors[1])
    Cosine = np.arccos(1 - cosine(Word_Vectors[0], Word_Vectors[1]))

    print word_1, Word_Vectors[0]
    print word_2, Word_Vectors[1]
    print 'The euclidean distance is %s' % Euclidean
    print 'The cosine distance is %s' % Cosine


# Extract_Process_Words_Interest('Test_Text.txt','Test_Text_1.txt','Test_Text_2.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.840B.300d.txt','Cluster_Centers_100.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.42B.300d.txt','Cluster_Centers_100.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.twitter.27B.100d.txt','Test_Text_2.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.twitter.27B.200d.txt','Test_Text_2.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.6B.50d.txt','Test_Text_2.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.6B.100d.txt','Test_Text_2.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.6B.200d.txt','Test_Text_2.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.6B.300d.txt','Test_Text_2.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.6B.50d.txt','Cluster_Centers_900.txt')
# Extract_Process_Words_Interest('geo-word2vec-glove-Wiki+GigaWord','glove.6B.50d.txt','Cluster_Centers_1000.txt')
