"""
Spectral_Embedding.py

Description
-----------
This file computes and plots the spectral embedding using sklearn.manifold.SpectralEmbedding for K-nearest neighbors
and sklearn.manifold.spectral_embedding for epsilon-neighborhoods. The input file containings items and their related
weights and is parsed using ProcessInput which creates a dictionary using items as keys and related weights as value.

Usage:

SE('Data.txt', ['E', 8])
Where E stands for the epsilon-neighborhoods and 5 for the maximum distance between two points for
them to be connected by an edge

However, epsilon-neighbrhoods do not seem to work well for embedding word vectors as the diagonals
generated have zeros in them, leading to eigenvalues obtained to be < 0. Not sure how accurate it is.


SE('Data.txt', ['N', 5])
Where N stands for the N neareest neighborhoods and 5 for the number of nearest neighbors wanted.


"""

from scipy import linalg as LA
from scipy.sparse import linalg as SparseLA
from ProcessInput import ProcessInput
from sklearn import manifold
from sklearn.utils.arpack import eigsh

import numpy as np
import matplotlib.pyplot as plt

def SE(filename, x):

    # Creates dictionary of items as keys and weights and values
    W_V = ProcessInput(filename)
    # print W_V

    if 'N' in x:
        return KNN(W_V, x[1])
    elif 'E' in x:
        # print W_V
        return ENBH(W_V, x[1])
    else:
        return 'Please enter a correct value for the method required and its associated value.'


def KNN(W_V, y):

    Distance = np.zeros([len(W_V), len(W_V)])

    A = np.zeros([len(W_V), len(W_V)])

    # Sets counter for rows
    Row = 0

    for key_1 in W_V:

        # Sets counter for columns
        Col = 0
        # print 'Row:', Row

        for key_2 in W_V:
            # Calculate L2 Norm for each value
            Distance[Row, Col] = LA.norm(W_V[key_1] - W_V[key_2], 2)
            Col += 1

        Val = np.sort(Distance[Row,:])
        # print Distance[Row,:]
        # print Val[1:(y+1)]

        Col = 0

        for v in Distance[Row,:]:
            if v in Val[1:(y+1)]:
                # print Row, Col
                A[Row, Col] = 1
                A[Col, Row] = 1
                Col += 1
            else:
                Col +=1
        # print A
        Row += 1

    # print Distance

    # print A

    D = np.diag(np.sum(A, 0))

    D_Inv_H = LA.pinv(D)**0.5

    # print D

    L = (D - A)

    N_L = np.dot(D_Inv_H, np.dot(L, D_Inv_H))

    # Ensures that matrices printed are aligned
    np.set_printoptions(precision=5, suppress=True)

    eig_values, eig_vectors = LA.eigh(L, D)

    # Check if decomposition is correct
    # Eig_D = np.diag(eig_values)
    # print Eig_D
    # L2 = np.dot(np.dot(eig_vectors, Eig_D), eig_vectors.T)
    # print L-L2

    order = eig_values.argsort()
    eig_values = eig_values[order]
    eig_vectors = eig_vectors[order]

    print eig_values

    x = eig_vectors[:, 1]
    y = eig_vectors[:, 2]
    # print x
    # print y

    N = range(len(x))

    plt.plot(x, y, 'bs')

    plt.autoscale()

    plt.show()

    '''
    # Collect Vectors
    for keys in W_V:
        X.append(W_V[keys])

    SE = manifold.SpectralEmbedding(n_neighbors=y)
    Y = SE.fit_transform(X)
    # print Y

    plt.scatter(Y[:, 0], Y[:, 1], cmap=plt.cm.Spectral)
    plt.axis('tight')
    plt.show()
    '''

def ENBH(W_V, y):

    # print y

    # Creates n by n matrix
    A = np.zeros([len(W_V), len(W_V)])

    # Sets counter for rows
    Row = 0

    # print A

    for key_1 in W_V:

        # Sets counter for columns
        Col = 0

        for key_2 in W_V:
            if np.array_equal(W_V[key_1], W_V[key_2]):
                # print LA.norm(W_V[key_1] - W_V[key_2], 2), 1
                A[Row, Col] = 0
                Col += 1
                # print A
            elif LA.norm(W_V[key_1] - W_V[key_2], 2) < y:
                # print LA.norm(W_V[key_1] - W_V[key_2], 2), 2
                A[Row, Col] = 1
                Col += 1
                # print A
            else:
                # print LA.norm(W_V[key_1] - W_V[key_2], 2), 3
                A[Row, Col] = 0
                Col += 1
                # print A

        Row += 1

    # A = np.array(np.matrix('[0 1 1 1 0 0 0 0; 1 0 0 1 0 0 0 0; 1 0 0 1 1 0 0 0; 1 1 1 0 0 0 0 0; 0 0 1 0 0 1 1 0; 0 0 0 0 1 0 1 1; 0 0 0 0 1 1 0 0; 0 0 0 0 0 1 0 0]')).astype('float64')

    # '''
    # To ensure that the diagonals are all non-zeros and thus can be solved, use D__
    D_ = np.sum(A, 0)

    for x in range(len(D_)):
        if D_[x] == 0:
            D_[x] = 1

    D__ =  np.diag(D_)
    # print D_
    # '''

    D = np.diag(np.sum(A, 0))

    D_Inv_H = LA.pinv(D)**0.5

    # print D

    L = (D - A)

    N_L = np.dot(D_Inv_H, np.dot(L, D_Inv_H))

    # Ensures that matrices printed are aligned
    np.set_printoptions(precision=5, suppress=True)

    eig_values, eig_vectors = LA.eigh(L, D__)

    # Check if decomposition is correct
    # Eig_D = np.diag(eig_values)
    # print Eig_D
    # L2 = np.dot(np.dot(eig_vectors, Eig_D), eig_vectors.T)
    # print L-L2

    order = eig_values.argsort()
    eig_values = eig_values[order]
    eig_vectors = eig_vectors[order]

    print eig_values

    x = eig_vectors[:, 1]
    y = eig_vectors[:, 2]
    # print x
    # print y

    N = range(len(x))

    plt.plot(x, y, 'bs')

    plt.autoscale()

    plt.show()

    '''
    SE = manifold.spectral_embedding(A, n_components=3)

    # print SE[:, 0]

    plt.plot(SE[:, 0], SE[:, 1], 'bs')
    plt.autoscale()
    plt.show()
    '''