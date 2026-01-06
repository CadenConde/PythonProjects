#1
def transpose_d(di):
    res = {}
    
    for i in range(len(di)):
        res[i] = set()
        
    for k, v in di.items():
        for n in v: 
            res[n].add(k)
            
    return res

#2
def top_sort(di):
    inDegs = {}
    res=[]
    
    for k,v in transpose_d(di).items(): # find indegrees
        inDegs[k] = len(v)
        
    while len(inDegs) > 0:
        for k, v in inDegs.items():
            if v == 0: # guarenteed to exist
                next = k 
                
        res.append(next) # remove and add to result
        inDegs.pop(next)
        
        for n in di[next]: # decrement indegrees from removed node
            inDegs[n] -= 1
        
    return res

#3
def greatest_weight_d(di):
    res = [-1, -1, -1]
    for k,v in di.items():
        for edge in v:
            if edge[1] > res[0]:
                res[0] = edge[1]
                res[1] = k
                res[2] = edge[0]
    return tuple(res)
    
#4
"""
    I didn't know if there was a standardized way to number edges, so my method is
    somewhat arbitrary, so my output looks slightly different, but it encodes the same info
"""
def dict_to_incidence(di):
    edges = set()
    for k,v in di.items():
        for n in v:
            if n >= k:
                edges.add((k, n))
    
    edgeList = list(edges) # list to give an order to edges
    
    res = [[0 for _ in range(len(edges))] for _ in range(len(di))]
    
    print(edgeList)
    
    for i in range(len(edgeList)):
        res[edgeList[i][0]][i] = 1
        res[edgeList[i][1]][i] = 1
        
    return res