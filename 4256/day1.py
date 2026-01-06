#1
def foo(n):
    res = 0
    for i in range(2,n,3):
        res+=n
    return res

#2
def sum_largest(li):
    maxN = float("-inf")
    maxN2 = float("-inf")
    for n in li:
        if n > maxN:
            maxN = n
            maxN2 = maxN
        elif n > maxN2:
            maxN2 = n
    
    return maxN+maxN2

#3
def sum_largest_sort(li):
    li2 = sorted(li)
    return li2[-1] + li2[-2]

#4a: first is faster, sorting is o(nLogn) time and first is just o(n)
#4b sorted returns a new list and leaves the original untouched, sort changes the original

#5
def merge(li1, li2):
    res = []
    p1 = 0
    p2 = 0
    while p2 < len(li2) and p1 < len(li1):
        if li2[p2] < li1[p1]:
            res.append(li2[p2])
            p2 += 1
        else:
            res.append(li1[p1])
            p1 += 1
            
    if p1 < len(li1):
        res += li1[p1:]
    elif p2 < len(li2):
        res += li2[p2:]
        
    return res

#6
def largest_so_far(li):
    res = 1
    cur = li[0]
    for i in range(1,len(li)):
        if li[i] > cur:
            cur = li[i]
            res += 1
    
    return res

#7
def evens(li):
    res = 0
    for i in range(0,len(li),2):
        if li[i] % 2 == 0:
            res += 1
            
    return res

#8
def linear_search(li, num):
    return num in li

#9
def binary_search(li, num):
    l = 0
    r = len(li) - 1
    while l<=r:
        m = (l+r)//2
        if li[m] == num:
            return True
        if li[m] < num:
            l = m+1
        else:
            r = m-1
            
    return False

#10: O(logn)