from collections import Counter
def most_vowels(string):
    strarr = string.lower().split()
    most = 0
    res = ""
    for s in strarr: 
        counts = Counter(s)
        c = counts['a'] + counts['e'] + counts['i'] + counts['o'] + counts['u'] + counts['y']
        if c > most:
            most, res = c, s
    return strarr[res]