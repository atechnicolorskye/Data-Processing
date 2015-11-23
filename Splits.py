from __future__ import division

import math
import os
import random

def SplitCorpus(filename, x):

    # Get working directory

    working_directory = os.getcwd()

    splits_directory = working_directory + '/' + filename[:-4] + '_Splits'

    # Check if new directory to be created exist

    if not os.path.exists(splits_directory):
        os.makedirs(splits_directory)

    # Number of lines in file

    number_lines = sum(1 for line in open(filename))

    # Number of splits required (assume blank lines between lines of text)

    number_files = int(math.ceil(number_lines / (2 * x)))


    count = range(1, number_files + 1)

    # Number of splits to be extracted per split

    count_lines = range(2 * x)

    with open(filename, 'r') as F:
        Input = F.readlines()

    # Change working directory to new directory

    os.chdir(splits_directory)

    for y in count:
        if y >= count[-1]:
            with open(filename[:-4] + '_' + str(y) + '.txt', 'w') as F:
                for lines in Input:
                    F.write(lines)
        else:
            with open(filename[:-4] + '_' + str(y) + '.txt', 'w') as F:
                for z in count_lines:
                    F.write(Input.pop(0))


def SplitTwitterNLP(filename):

    # Obtain tweets

    with open(filename, 'r') as F:
        Input = F.readlines()

    # Aggregrate tweets

    Tweets = []

    current_line = []

    for line in Input:
        if line == '\t\n':
            Tweets.append(current_line)
            current_line = []
        else:
            current_line.append(line)

    # Calcuate training, validation and test splits

    total_tweets = len(Tweets)

    size_set_1 = math.floor(0.25 * len(Tweets)) # Sets 2 and 3 are the same size as set 1

    size_set_4 = total_tweets - 3 * math.floor(0.25 * len(Tweets))

    print "The size of the sets 1, 2, 3 is " + str(size_set_1) + " and the size of set 4 is " + str(size_set_4)

    # Obtain validation and test splits

    Split_1 = []

    Split_2 = []

    Split_3 = []

    while len(Split_1) < size_set_1:
        split_1_tweet = Tweets.pop(random.randint(0, len(Tweets)-1))
        Split_1.append(split_1_tweet)
        split_2_tweet = Tweets.pop(random.randint(0, len(Tweets)-1))
        Split_2.append(split_2_tweet)
        split_3_tweet = Tweets.pop(random.randint(0, len(Tweets)-1))
        Split_3.append(split_3_tweet)

    # print "The size of the training set is " +str(len(Tweets))

    # print "The size of the validation set is " + str(len(Validation))

    # print "The size of the test set is " +str(len(Test))

    print "The size of set 1 is " + str(len(Split_1))

    print "The size of set 2 is " + str(len(Split_2))

    print "The size of set 3 is " + str(len(Split_3))

    print "The size of set 3 is " + str(len(Tweets))

    # Write splits to file

    with open(filename[:-4] + '_123.txt', 'w') as Training_1:
        Combined_123 = Split_1 + Split_2 + Split_3
        for tweet in Combined_123:
            Training_1.write('\n')
            for line in tweet:
                Training_1.write(line)

    with open(filename[:-4] + '_124.txt', 'w') as Training_2:
        Combined_124 = Split_1 + Split_2 + Tweets
        for tweet in Combined_124:
            Training_2.write('\n')
            for line in tweet:
                Training_2.write(line)

    with open(filename[:-4] + '_134.txt', 'w') as Training_3:
        Combined_134 = Split_1 + Split_3 + Tweets
        for tweet in Combined_134:
            Training_3.write('\n')
            for line in tweet:
                Training_3.write(line)

    with open(filename[:-4] + '_234.txt', 'w') as Training_4:
        Combined_234 = Split_2 + Split_3 + Tweets
        for tweet in Combined_234:
            Training_4.write('\n')
            for line in tweet:
                Training_4.write(line)

    with open(filename[:-4] + '_1.txt', 'w') as S1:
        for tweet in Split_1:
            S1.write('\n')
            for line in tweet:
                S1.write(line)

    with open(filename[:-4] + '_2.txt', 'w') as S2:
        for tweet in Split_2:
            S2.write('\n')
            for line in tweet:
                S2.write(line)

    with open(filename[:-4] + '_3.txt', 'w') as S3:
        for tweet in Split_3:
            S3.write('\n')
            for line in tweet:
                S3.write(line)

    with open(filename[:-4] + '_4.txt', 'w') as S4:
        for tweet in Tweets:
            S4.write('\n')
            for line in tweet:
                S4.write(line)

# SplitCorpus('NUS_smsCorpus_EN_2015_03_09_Tok_Line_Space.txt', 100)
# SplitTwitterNLP('ner.txt')