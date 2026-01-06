def identity(n):
    res = []
    for i in range(n):
        res.append([0] * n)
        res[i][i] = 1
    return res

def columns(m,n):
    res = []
    for i in range(m):
        res.append([0] * n)
        for j in range((n+1)//2): # find number of valid columns needed
            res[i][2*j] = i + (j*m) + 1 # set each column to 1+row+(column*m)
    return res

import numpy as np
def identity2(n):
    return np.identity(n)