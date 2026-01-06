#1
def median(li):
    if (len(li) & 1) == 1:
        return sorted(li)[len(li)//2]
    else:
        return (sorted(li)[len(li)//2] + sorted(li)[(len(li)//2) - 1]) / 2
    
#2
def mode(li):
    modes = {}
    res = set()
    maxN = 0
    
    #find modes
    for n in li:
        if not n in modes:
            modes[n] = 1
        else:
            modes[n] += 1
            maxN = max(modes[n], maxN)
    
    #find all with most occurance
    for k,v in modes.items():
        if v == maxN:
            res.add(k)
            
    return res
        
#3
def arithmetic_mean(li):
    res = 0
    for n in li:
        res += n
    return res/len(li)

#4
def olympic_mean(li):
    res = 0
    maxi = li[0]
    mini = li[0]
    
    for n in li:
        mini = min(mini, n)
        maxi = max(maxi, n)
        res += n
        
    return (res-maxi-mini)/(len(li)-2)

#5
# floating point makes this annoying, I could round if needed, but math is correct
def geometric_mean(li):
    res = 1
    for n in li:
        res *= n
    return res ** (1/len(li))

#6
def harmonic_mean(li):
    div = 0
    for n in li:
        div += (1/n)
    return len(li)/div

#7
def sample_variance(li):
    mean = arithmetic_mean(li)
    res = 0
    for n in li:
        res += (n - mean)**2
    return res*(1/(len(li)-1))
    
