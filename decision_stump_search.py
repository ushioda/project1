# -*- coding: utf-8 -*-

# input: 
# x = a vector of feature j sorted across observations.
# y = label 
# w = weights



import numpy as np

def search(x, y, w):
    
    # edge for constant classifier
    edge_0 = np.dot(y, w)
    
    # set initial best edge
    edge_star = edge_0
    
    # set initial edge
    edge = edge_0
    
    for i in range(1, len(x)):
            edge = edge - 2 * y[i - 1] * w[i - 1]
            if not x[i - 1] = x[i]:
                if abs(edge) > abs(edge_star):
                    edge_star = edge
                    