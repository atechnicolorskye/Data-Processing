"""
Extract_Compare.py

Description
-----------
This file compares the Euclidean and Cosine similiaritys of word vectors processed by different methods and 
outputs a file containing the comparisons. The input file is assumed to contain words followed by a list containing
their coordinates.

Usage:
Compare_All_Short('Foo.txt'),outputs 'Word_Vectors_Compared_' + input filename
"""

import numpy as np
import re

from scipy.spatial.distance import euclidean
from sklearn.metrics.pairwise import cosine_similarity

# def Compare_All_Short_1(Word_Vectors):

#     '''
#     with open(filename, 'r') as F:
#         Input = F.readlines()

#     Word_Vectors = {}

#     # K = int(filename[23:-4])

#     # Sum_Vectors = np.zeros((1,K))

#     for line in Input:
#         y__ = re.sub(',', '', line)
#         y_ = y__.split(' ')
#         # print y_
#         # print len(y_)
#         y_[1] = re.sub('\[', '', y_[1])
#         # print y_[1]
#         y_[-1] = re.sub('\]', '', y_[-1])
#         y = y_[1:]
#         # print y
#         z_ = map(float, y)
#         z = np.array(z_)
#         Word_Vectors[y_[0]] = z
#         # Sum_Vectors += z

#     # print Sum_Vectors
#     '''
#     Word_List_1 = Word_Vectors.keys()
#     Word_List_2 = Word_Vectors.keys()

#     # print Word_Vectors

#     # for word in Word_List_1:
#     #     Word_Vec = Sum_Vectors - Word_Vectors[word]
#     #     Word_Vectors[word] = Word_Vec / np.sum(Word_Vec)

#     # print Word_Vectors

#     with open('Word_Vectors_Compared_' + filename[13:-4] + '.txt', 'w') as C:
#         for word_1 in Word_List_1:
#             Word_List_2.remove(word_1)

#             if len(Word_List_2) > 0:

#                 for word_2 in Word_List_2:
#                     Euclidean = euclidean(Word_Vectors[word_1], Word_Vectors[word_2])
#                     Cosine = cosine_similarity(Word_Vectors[word_1], Word_Vectors[word_2])

#                     C.write(str(word_1) + ', ' + str(word_2) + '\n')
#                     C.write('The euclidean distance is ' + str(Euclidean) + '\n')
#                     C.write('The cosine similarity is ' + str(Cosine) + '\n')

#     print 'Comparison for K = ' + filename[13:-4] + ' has been completed!'

    # Word_List_1.sort()
    # print Word_List_1

def Compare_All_Short(filename):

    with open(filename, 'r') as F:
        Input = F.readlines()

    Word_Vectors = {}

    for line in Input:
        y_ = line.split(',')
        y_[0] = re.sub('[^\w]', '', y_[0])
        y_[1] = re.sub('\[', '', y_[1])
        y_[-1] = re.sub('\] \]', '', y_[-1])
        y = y_[1:]
        z = map(float, y)
        Word_Vectors[y_[0]] = z

    Word_List_1 = Word_Vectors.keys()
    Word_List_2 = Word_Vectors.keys()

    with open('Word_Vectors_Compared_' + filename[:-4] + '.txt', 'w') as C:
    # with open('Word_Vectors_Compared_' + filename[13:-4] + '.txt', 'w') as C:
        for word_1 in Word_List_1:
            Word_List_2.remove(word_1)

            if len(Word_List_2) > 0:

                for word_2 in Word_List_2:
                    Euclidean = euclidean(Word_Vectors[word_1], Word_Vectors[word_2])
                    Cosine = np.arccos(1 - cosine(Word_Vectors[word_1], Word_Vectors[word_2]))

                    C.write(str(word_1) + ', ' + str(word_2) + '\n')
                    C.write('The euclidean distance is ' + str(Euclidean) + '\n')
                    C.write('The cosine distance is ' + str(Cosine) + '\n')

    print 'Comparison for K = ' + filename[:-4] + ' has been completed!'
    # print 'Comparison for K = ' + filename[13:-4] + ' has been completed!'

# def Compare_All_Long(filename):

#     with open(filename, 'r') as F:
#         Input = F.readlines()

#     Word_Vectors = {}

#     for line in Input:
#         y_ = line.split(',')
#         y_[0] = re.sub('[^\w]', '', y_[0])
#         y_[1] = re.sub('\[', '', y_[1])
#         y_[-1] = re.sub('\] \]', '', y_[-1])
#         y = y_[1:]
#         z = map(float, y)
#         Word_Vectors[y_[0]] = z

#     Word_List_1 = Word_Vectors.keys()
#     Word_List_2 = Word_Vectors.keys()

#     with open('Word_Vectors_Compared_' + filename[23:-4] + '.txt', 'w') as C:
#         for word_1 in Word_List_1:
#             Word_List_2.remove(word_1)

#             if len(Word_List_2) > 0:

#                 for word_2 in Word_List_2:
#                     Euclidean = euclidean(Word_Vectors[word_1], Word_Vectors[word_2])
#                     Cosine = np.arccos(1 - cosine(Word_Vectors[word_1], Word_Vectors[word_2]))

#                     C.write(str(word_1) + ': ' + str(Word_Vectors[word_1]) + '\n')
#                     C.write(str(word_2) + ': ' + str(Word_Vectors[word_2]) + '\n')
#                     C.write('The euclidean distance is ' + str(Euclidean) + '\n')
#                     C.write('The cosine distance is ' + str(Cosine) + '\n')

#     print 'Comparison for K = ' + filename[23:-4] + ' has been completed!'

# Compare_All_Short_1('Word_Vectors_Norm_1_1000.txt')
# Compare_All_Short_1('Word_Vectors_Dot_1000.txt')
# Compare_All_Short_1('Word_Vectors_Divided_1000.txt')
# Compare_All_Short_1('Word_Vectors_Divided_Abs_1000.txt')
# Compare_All_Short_1('Word_Vectors_Added_Absolute_1000.txt')
# Compare_All_Short_1('Word_Vectors_Added_Absolute_All_1000.txt')
# Compare_All_Short_1('Word_Vectors_Normalized_1000.txt')


# Compare_All_Short_1('Interested_Vectors_Words.txt')
# Compare_All_Short_1('Word_Vectors_Normalized_500.txt')
# Compare_All_Short_1('Word_Vectors_Normalized_600.txt')
# Compare_All_Short_1('Word_Vectors_Normalized_700.txt')
# Compare_All_Short_1('Word_Vectors_Normalized_800.txt')
# Compare_All_Short_1('Word_Vectors_Normalized_900.txt')
