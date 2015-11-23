"""
K_Means.py

Description
-----------
This file computes K-means via sklean.cluster.KMeans and plots the results using Matplotlib. The input file containing
items and their related weights and is parsed using ProcessInput which creates a dictionary using items as keys and
related weights as value.

Usage:
run_KMeans('glove.6B.50d.txt', 10)
10 is K, the number of required clusters
"""


import matplotlib.pyplot as plt
import numpy as np
# import csv

from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

from ProcessInput import ProcessInput

def run_KMeans(Raw_Data, K):

    Intermediate_Data = ProcessInput(Raw_Data)

    Keys = Intermediate_Data.keys()

    Data = []

    for x in Intermediate_Data:
        Data.append(Intermediate_Data[x])

    X = KMeans(n_clusters=K)
    Y = X.fit_transform(Data)
    Labels = X.labels_

    # print Y

    centroids = X.cluster_centers_

    with open('Cluster_Centers_'+ str(K) + '.txt', 'w') as C:
        # writer = csv.writer(C, lineterminator='\n')
        # writer.writerows(centroids)

        for line in centroids:
            if ']' in str(line):
                line_ = str(line)
                C.write(line_[:-1]+' ]\n')
            else:
                C.write(str(line)+'\n')

        # for line in centroids:
        #     Z = '['
        #     for item in line:
        #         Z += str(item)+', '
        #     Z = Z[:-2] + ']'
        #     print >> C, Z

    # C.writelines(centroids)

    # C.close()
    # C.flush()
    # os.fsync(f.fileno())

    Normal_Euclidean_Distances = []
    # print Normal_Euclidean_Distances

    for Z in range(len(Data)):
        Euclidean_Distances = [euclidean(Data[Z], Centroid) for Centroid in centroids]
        # print Euclidean_Distances
        Sum = sum(Euclidean_Distances)
        # print Sum
        Normal_Euclidean_Distances_ = [Keys[Z], [Euclidean_Distance/Sum for Euclidean_Distance in Euclidean_Distances]]
        Normal_Euclidean_Distances.append(Normal_Euclidean_Distances_)
        # print [Euclidean_Distance/Sum for Euclidean_Distance in Euclidean_Distances]

    # print Normal_Euclidean_Distances

    with open('Normalized_Euclidean_Distances_'+ str(K) + '.txt', 'w') as N:

        for line in Normal_Euclidean_Distances:
            if ']' in str(line):
                line_ = str(line)
                N.write(line_[:-1]+' ]\n')
            else:
                N.write(str(line)+'\n')

    plt.scatter(Y[:, 0], Y[:, 1], c=Labels.astype(np.float))
    # plt.scatter(centroids[:, 0], centroids[:, 1], marker='x',
    #             s=169, linewidths=3, color='k', zorder=10)
    plt.autoscale()
    # plt.show()
    plt.savefig('Cluster_Centers_'+ str(K) + '.png', bbox_inches='tight')



# run_KMeans('Test_Text.txt', 2)

# run_KMeans('glove.6B.50d.txt', 100)
# run_KMeans('glove.6B.50d.txt', 300)
# run_KMeans('glove.6B.50d.txt', 500)
# run_KMeans('glove.6B.50d.txt', 700)
# run_KMeans('glove.6B.50d.txt', 900)


