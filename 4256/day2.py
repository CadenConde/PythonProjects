#1a
def anti_diag(n):
    res = []
    for i in range(n):
        row = [0] * n
        row[n-i-1] = 1
        res.append(row)
    return res

#1b
import numpy as np
def anti_diag2(n):
    res = np.identity(5)
    return np.flip(res, 0)

#1c
def anti_diag3(n):
    res = np.identity(5)
    return np.rot90(res)

#1d
def anti_diag4(n):
    res = np.identity(5)
    return np.flipud(res)

#2
def border(m,n):
    res = [[0] * n for _ in range(m)]
    i = 1 
    for r in range(len(res[0])):
        res[0][r]  = i
        i += 1
    for c in range(1,len(res)):
        res[c][-1] = i
        i += 1
    for r in range(len(res[0])-2,-1,-1):
        res[-1][r] = i
        i += 1
    for c in range(len(res)-2,0,-1):
        res[c][0] = i
        i += 1    
    return res

#3a
def transpose(arr):
    res = [[0]*len(arr) for _ in range(len(arr[0]))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = arr[j][i]
    return res
#3b
def transpose2(arr):
    return np.transpose(arr)

#4a
def dot_prod(l1,l2):
    res = 0
    for n1,n2 in zip(l1,l2):
        res += n1*n2
    return res

#4b 
def dot_prod2(l1,l2):
    return np.dot(l1,l2)

#5a
def is_u_t(mat):
    for i in range(len(mat[0])):
        for j in range(i+1, len(mat)):
            if not mat[j][i] == 0:
                return False
    return True

#5b
def is_u_t2(mat):
    tri = np.triu(mat)
    return np.array_equal(mat, tri)

#6
def chessboard(n):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = (i+j-1)%2
    return res

#7
def is_toeplitz(mat):
    for i in range(len(mat[0])):
        j = 0
        n = mat[j][i]
        while i < len(mat[0])-1 and j < len(mat)-1:
            i += 1
            j += 1
            if mat[j][i] != n:
                return False
    for j in range(1,len(mat)):
        i = 0
        n = mat[j][i]
        while i < len(mat[0])-1 and j < len(mat)-1:
            i += 1
            j += 1
            if mat[j][i] != n:
                return False
    return True
     

# print(is_toeplitz([[1, 2, 5, 4],[6, 1, 2, 5],[2, 6, 1, 2],[3, 2, 6, 1]]))