#1 cycle graph of n nodes as a matrix
def cycle_m(n):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][(i+1)%n] = 1
        res[i][i-1] = 1
    return res

#2 same as a dict
def cycle_d(n):
    res = {}
    for i in range(n):
        res[i] = {(i-1)%n, (i+1)%n}
    return res

#3 check if mat is regular (all nodes of same deg)
def is_regular_m(mat):
    deg = 0
    for i in mat[0]:
        deg += i
    for i in mat:
        test = 0
        for j in i:
            test += j
        if test != deg:
            return False
    return True

#4 same with dict
def is_regular_d(di):
    for k,v in di.items():
        if len(v) != len(di[0]):
            return False
    return True
        
#5 comp. bart. with m and n nodes. check preclass reading if confused.
def complete_bipartite_d(m,n):
    res = {}
    for i in range(m):
        res[i] = set(range(m, n+m))
    for i in range(m, n+m):
        res[i] = set(range(m))  
    return res  

#6 same with dict
def complete_bipartite_m(m,n):
    res = [([0]*m + [1]*n) for _ in range(m)]
    res.append([([1]*m + [0]*n) for _ in range(n)])
    return res

#7 self explainitory
def di_to_mat(di):
    res = [[0]*len(di) for _ in range(len(di))]
    for k,v in di.items():
        for n in v:
            res[k][n] = 1
    return res
        
#8 literally ripped this off preclass and changed 3 lines, adapt it to work with dat instead of dih
from collections import deque
def bfs_m(mat, start_node=0):
    visited_nodes = deque()
    result = [None] * len(mat)
    result[start_node] = 0
    visited_nodes.append(start_node)
    while visited_nodes:
        node = visited_nodes.popleft()
        for adjacent_node in range(len(mat[node])):
            if mat[node][adjacent_node] == 1:
                if result[adjacent_node] is None:
                    result[adjacent_node] = result[node] + 1
                    visited_nodes.append(adjacent_node)
    return result