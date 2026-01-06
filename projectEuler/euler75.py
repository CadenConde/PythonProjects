'''
Given that L is the length of the wire, for how many values of L <= 1_500_000 can exactly one integer sided right angle triangle be formed?

For full problem, see here:
https://projecteuler.net/problem=75
'''

import math
from collections import defaultdict

# snag primitive pythagorean triple generator from someone smarter than me
# (I had a working one but my math was suboptimal, this is better)
def genTriples(k):
    n,m = 1,2
    while m<=k:                  # while z<k (for largest m producing z)
        if n>=m: n,m = m%2,m+1      # n reached m, advance m, reset n
        z = m*m+n*n                 # compute z 
        if z >= k: n=m;continue     # skip remaining n when z >= k
        if math.gcd(n,m) == 1:           # trigger on coprimes
            yield m*m-n*n,2*m*n,z   # return x,y,z triple
        n += 2 
        

n = 1_500_000
m = defaultdict(int)

c = 0
for x,y,z in genTriples(n/2):
    sum = x+y+z   
    temp = sum

    if sum > n*2:
        break
    
    while sum <= n:
        m[sum] += 1
        if m[sum] == 1:
            c +=1
        elif m[sum] == 2:
            c-=1
        sum += temp

print(c)
   


                




    
