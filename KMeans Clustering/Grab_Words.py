def GrabWords(filename):
    # Create an empty list
    Words = []

    # Read file
    F = open(filename, "r")
    Input = F.readlines()
    # print Input
    F.close

    Words_Rows = [0]

    X = 0

    while X < 2748:
        X += 3
        Words_Rows.append(X)

    for number in Words_Rows:
        words = Input[number].split()
        for word in words:
            if word not in Words:
                Words.append(word)

    print len(Words)

    # print str(sorted(Words))

    with open('New_Words_Interest.txt','w') as File:
        File.write(str(sorted(Words)))

def GrabSentences(filename):
    # Create an empty list
    Sentences = []

    # Read file
    F = open(filename, "r")
    Input = F.readlines()
    # print Input
    F.close

    Sentences_Rows = [0]

    X = 0

    while X < 2748:
        X += 3
        Sentences_Rows.append(X)

    with open('New_Sentences_Interest.txt','w') as File:
        for number in Sentences_Rows:
            File.write(str(Input[number]))

def CheckWords(filename):
    # Create an empty list
    Words = []

    # Read file
    F = open(filename, "r")
    Input = F.readlines()
    # print Input
    F.close

    for lines in Input:
        if '[' in lines:
            # print lines
            word = lines.split()
            Words.append(word[0])

    print Words


CheckWords('Word2Vec_50_New_Sentences_Interest.txt')