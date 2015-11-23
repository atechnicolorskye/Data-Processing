"""
ProcessInput.py

Description
-----------
This file reads an input file containing words and their associated vectors. The input format is 'Word [Vector]'. The words
and their vectors are stored in an empty dictionary with words being keys and vectors value.

"""

import re
import numpy as np

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
        y[1] = re.sub('\[', '', y[1])
        y[-1] = re.sub('\]', '', y[-1])
        # print y
        z = map(float, y[1:])
        W_V[y[0]] = np.array(z)

    # len(W_V)
    # print W_V["'s"]
    return W_V