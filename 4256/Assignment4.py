from random import randint
def ten_flips():
    heads = 0
    for _ in range(10):
        if randint(0,1) == 1:
            heads += 1
    return heads == 7

def prob_seven_out_of_ten(n):
    count = 0
    for _ in range(n):
        if ten_flips():
            count += 1
    return count/n 

print(prob_seven_out_of_ten(1000))