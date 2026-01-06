from random import uniform, randint, choices
import math
#1
def circle(n):
    hits = 0
    for _ in range(n):
        x = uniform(-1,1)
        y = uniform(-1,1)
        if math.sqrt(x*x + y*y) <= 1:
            hits +=1
    return (hits/n)*4

#2
def ice_cream(trials):
    hits = 0
    for _ in range(trials):
        bill = uniform(0,30)
        lilly = uniform(0,30)
        if bill <= lilly and lilly-bill <= 5:
            hits += 1
        elif lilly <= bill and bill - lilly <= 7:
            hits+=1
    return round(hits/trials,2)
        
#3
def matches(trials):
    def matches_helper():
        res = 0
        box1 = 20
        box2 = 20
        while box1 > 0 and box2 > 0:
            if randint(0,1) == 0:
                box1 -= 1
            else:
                box2 -= 1
            res += 1
        return res
    
    res = 0
    for _ in range(trials):
        res += matches_helper()
    return res / trials

#4a
def dice_rolls(trials):
    res = {i : 0 for i in range(2,13)}
    for _ in range(trials):
        res[randint(1,6) + randint(1,6)] += 1
    for k,v in res.items():
        res[k] /= trials
        res[k] *= 100
        res[k] = round(res[k],1)
    return res

#4b
def dice_rolls2(trials,n):
    res = {i : 0 for i in range(n,6*n+1)}
    
    for _ in range(trials):
        sum = 0
        for _ in range(n):
            sum += randint(1,6)
        res[sum] += 1
        
    for k,v in res.items():
        res[k] /= trials
        res[k] *= 100
        res[k] = round(res[k],1)
    return res

#4c
def dice_rolls3(trials):
    bias = [1,1,2,2,3,3,4,5,6]
    res = {i : 0 for i in range(2,13)}
    for _ in range(trials):
        res[choices(bias)[0] + choices(bias)[0]] += 1
    for k,v in res.items():
        res[k] /= trials
        res[k] *= 100
        res[k] = round(res[k],1)
    return res

#5
def birthday():
    res = 0
    for _ in range(100_000):
        bdays= set()
        day = randint(1,366)
        while not day in bdays:
            bdays.add(day)
            day = randint(1,366)
            res += 1
    return res/100_000

#6
# the same, because the trials are independent, 
# you have the same likelyhood of getting any number to follow any other

#7
def my_cos(trials):
    res = 0
    for _ in range(trials):
        x = uniform(0, math.pi/2)
        y = uniform(0,3)
        if y <= math.cos(x) + 2:
            res += 1
    res /= trials
    return res * 3 * (math.pi/2)

print(my_cos(100000))