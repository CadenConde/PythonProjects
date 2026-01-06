# Caden Conde 4256 Assignment 1
# assuming good user input so no error checking, 
# let me know if you want it different next time

def maximum(li):
    res = li[0]
    for i in li:
        if i > res: 
            res = i
    return res

def maximum_index(li):
    res = 0
    for i in range(len(li)):
        if li[i] > li[res]:
            res = i
    return res
