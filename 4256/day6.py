#1a
def union(s1,s2):
    res = s2
    for n in s1:
        if not n in res:
            res.add(n)
    return res

#1b
def difference(s1,s2):
    res = s1
    for n in s2:
        if n in res:
            res.remove(n)
    return res

#1c
def is_subset(s1,s2):
    for n in s2:
        if not n in s1:
            return False
    return True

#1d
def is_disjoint(s1,s2):
    for n in s2:
        if n in s1:
            return False
    return True

#1e
def symmetric_difference(s1,s2):
    res = s2
    for n in s1:
        if n in res:
            res.remove(n)
        else:
            res.add(n)
    return res

#1f
def cartesian_product(s1,s2):
    res = set()
    for n in s1:
        for m in s2:
            res.add((n,m))
    return res

#2a
def union_2(*s1):
    res = set()
    for s in s1:
        for n in s:
            if not n in res:
                res.add(n)
    return res

#2b
def is_disjoint_2(*s1):
    return len(union_2(*s1)) == sum(len(s) for s in s1)

#3
#"str" is a function so I went with s
def is_well_formed(s):
    stack = []
    mapping = {'{':'}','[':']','(':')'}
    for par in s:
        if par in mapping:
            stack.append(par)
        elif len(stack) == 0:
            return False
        else:
            if not mapping[stack.pop(len(stack)-1)] == par:
                return False
    return len(stack) == 0

#4
def rpn(s):
    stack = []
    # convert string to stack
    for i in range(len(s)-1,-1,-1):
        stack.append(s[i])
    #get first digit
    res = int(stack.pop())
    while(stack):
        #remove 2 at a time until stack is clear
        digit = int(stack.pop())
        oper = stack.pop()
        match oper:
            case '+':
                res += digit
            case '-':
                res -= digit
            case '*':
                res *= digit
            case '/':
                res /= digit
    return res
    
print(rpn("12-3*1+"))
        