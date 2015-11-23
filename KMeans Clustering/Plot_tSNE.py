"""
Plot_tSNE.py

Description
-----------
This file extracts cluster centres or word vectors and plots them using tSNE.

Usage:
To plot just from one file:
Plot_TSNE('File.txt', 'c')
To plot clusters centres, set second input as 'c'
To plot word vectors, set second input as 'w'

Plot_Combined_TSNE('File_1.txt','File_2.txt',c)
To plot clusters centres, set second input as 'c'
To plot word vectors, set second input as 'w
"""


import matplotlib.pyplot as plt
import numpy as np
import re

from tsne import bh_sne
# from ProcessInput_ import ProcessInput


def Extract_Clusters(x):

    # To add normal

    with open(x, 'r') as C:
        Clusters = C.readlines()

    Cluster_List = []

    for Cluster in Clusters:
        # print Cluster
        if '[' in Cluster:
            z = []
            String_To_List(Cluster, z)
            # print z
        elif ']' in Cluster:
            String_To_List(Cluster, z)
            # print z
            Cluster_List.append(np.array(z))
            z = []
        else:
            String_To_List(Cluster, z)
            # print z

    for cluster in Cluster_List:
        len(cluster)

    # print Cluster_List

    return Cluster_List


def String_To_List(STL, z):

    # print STL.split(' ')

    for Val in STL.split(' '):
        if '[' in Val:
            # print Val
            try:
                z.append(float(Val[1:]))
            except ValueError:
                pass
        elif ']' in Val:
            # print Val
            # print Val[:-2]
            try:
                z.append(float(Val[:-2]))
            except ValueError:
                pass
        else:
            try:
                z.append(float(Val))
            except ValueError:
                pass

def Extract_Word_Vectors(x):

    with open(x, 'r') as F:
        Input = F.readlines()

    Z = []

    for line in Input:
        y__ = re.sub(',', '', line)
        y_ = y__.split(' ')
        # print y_
        # print len(y_)
        y_[1] = re.sub('\[', '', y_[1])
        # print y_[1]
        y_[-1] = re.sub('\]', '', y_[-1])
        y = y_[1:]
        # print y
        z_ = map(float, y)
        Z.append(np.array(z_))

    # print Z

    return Z


def Plot_TSNE(x, T):

    if T = c:
        Z = Extract_Clusters(x)
    else:
        Z = Extract_Word_Vectors(x)

    N = range(len(Z))

    N.pop(0)

    # print N

    D = len(Z[0])

    print D

    M = Z[0]

    for x in N:
        M = np.vstack((M, Z[x]))

    Y = bh_sne(M)

    plt.scatter(Y[:, 0], Y[:, 1])
    plt.autoscale()
    plt.show()


def Plot_Combined_TSNE(x,y,c):

    if T = c:
        Z_1 = Extract_Clusters(x)
        Z_2 = Extract_Clusters(y)
    else:
        Z_1 = Extract_Word_Vectors(x)
        Z_2 = Extract_Word_Vectors(y)

    N_1 = range(len(Z_1))

    N_1.pop(0)

    M_1 = Z_1[0]

    for x in N_1:
        M_1 = np.vstack((M_1, Z_1[x]))

    Y_1 = bh_sne(M_1)

    N_2 = range(len(Z_2))

    N_2.pop(0)

    M_2 = Z_2[0]

    for x in N_2:
        M_2 = np.vstack((M_2, Z_2[x]))

    Y_2 = bh_sne(M_2)

    plt.scatter(Y_1[:, 0], Y_2[:, 1], c='g', marker='o', label='Absolute Vectors')
    plt.scatter(Y_2[:, 0], Y_2[:, 1], c='r', marker='s', label='Non-absolute Vectors')
    plt.legend()
    plt.autoscale()
    plt.show()

# Extract_Word_Vectors_2('Word_Vectors_Divided_100.txt')
# Plot_Combined_TSNE('Word_Vectors_Norm_1_1000.txt','Word_Vectors_Norm_2_1000.txt')