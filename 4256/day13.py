import numpy as np

#1
def row_sums(arr):
    return arr.sum(axis=0)

#2
def forty_two(arr):
    out = arr.copy()
    out[(out < 0) & (out % 2 == 1)] = 42
    return out

#3
def make_grid(n, m):
    return np.arange(1, n*m+1).reshape(n,m)

#4
#I think this is what you want? I was a bit confused by the directions
def slicer(arr):
    return arr[::2, 0:3]
