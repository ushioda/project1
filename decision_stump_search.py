# -*- coding: utf-8 -*-

# input: 
#   features = numpy array matrix of features
#              each column represents a single observation
#   y =    labels
#   w =  weights

# output:
# feature, polarity and threshold

import numpy as np
from operator import itemgetter
import math

def search(features, y, w):
    
    # number of features
    
    J = len(features[:,0])
    
    # number of samples
    
    N = len(y)
    
    # reconstruct features into pairs not to loose order of data
    
    X = []
    sample_index = np.array(range(N))
    for j in range(J):
        value = features[j]
        x = zip(sample_index, value)
        x = sorted(x, key = itemgetter(1))
        X.append(x)
        
    
    # edge for constant classifier
    edge_0 = np.dot(y,w)
    
    # set initial best edge
    edge_star = edge_0
    
    # set feature value
    j_star = 0
        
    for j in range(J):
        # set initial edge
        edge = edge_0            
        for i in range(1, N):
            index = X[j][i][0]
            edge = edge - 2 * y[index - 1] * w[index - 1]
            if not X[j][i - 1][1] == X[j][i][1]:
                if abs(edge) > abs(edge_star):
                    edge_star = edge
                    j_star = j
                    theta_star = (X[j][i - 1][1] + X[j][i][1]) / 2
    
    stump = [j_star, theta_star, math.copysign(1, edge_star)]
    return stump
