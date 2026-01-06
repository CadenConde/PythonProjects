#1
from collections import Counter
def vowels(sentence):
    strarr = sentence.lower().split()
    most = 0
    res = {}
    for s in strarr: 
        counts = Counter(s)
        c = counts['a'] + counts['e'] + counts['i'] + counts['o'] + counts['u'] + counts['y']
        if c > most:
            most = c
            res = {s}
        elif c == most:
            res.add(s)
    return res
    

#2
def first_unique_char(s):
    c = Counter(s)
    for l in s:
        if c[l] == 1:
            return l
    return None

#3
def are_isomorphic(s1, s2):
    mapping = {}
    seen = set()
    for a,b in zip(s1,s2):
        if not a in mapping and not b in seen:
            mapping[a] = b
            seen.add(b)
        elif not a in mapping or mapping[a] != b:
            return False
    return True

#4
def is_pal(s, left = 0, right = None):
    if right == None:
        right = len(s)-1
    if right - left <= 1:
        return True
    if s[left] == s[right]:
        return is_pal(s, left+1, right-1)
    return False
    
#5
def shift_encipher(string, shift):
    res = ""
    for c in string:
        if c == " ":
            res = res + " "
        else:
            res = res + chr(((ord(c)-65+shift)%26) + 65)
    return res

#6
def shift_decipher(string, shift):
    res = ""
    for c in string:
        if c == " ":
            res = res + " "
        else:
            res = res + chr(((ord(c)-65-shift)%26) + 65)
    return res

#7
def rail_encipher(string):
    res = ""
    for i in range(0, len(string), 2):
        res = res + string[i]
    for i in range(1, len(string), 2):
        res = res + string[i]
    return res

#8  
def rail_decipher(string):
    res = ""
    
    # if string length is odd, just manually deal with the mid char
    c = 0
    if(len(string) % 2 == 1):
        c = 1
    
    # that logic is needed because zip will delete data otherwise
    for a, b in zip(string[0:(len(string)//2)], string[len(string)//2+c:]):
        res = res + a + b
        
    # manually add middle char back
    if c == 1:
        res = res + string[len(string)//2]
        
    return res

print(rail_decipher(rail_encipher("ATTACKATDAWN")))