#1
def grades(di):
    res = {}
    for k,v in di.items():
        resGrade = 'E'
        if v >= 90:
            resGrade = 'A'
        elif v >= 80:
            resGrade = 'B'
        elif v >= 70:
            resGrade = 'C'
        elif v >= 60:
            resGrade = 'D'
        res[k] = resGrade
    return res

#2
def letter_grades(di):
    res = {'A' : 0,'B' : 0,'C' : 0,'D' : 0,'E' : 0}
    for k,v in di.items():
        res[v] += 1
    return res

#3
def letter_grades2(di):
    res = {'A' : set(),'B' : set(),'C' : set(),'D' : set(),'E' : set()}
    for k,v in di.items():
        res[v].add(k)
    return res

#4
def highest_scores(di):
    res = set()
    high = 0
    for k,v in di.items():
        for n in v:
            if n > high:
                high = n
                res.clear()
            if n == high:
                res.add(k)
    return res

#5
def course_average(di):
    res = {}
    for k,v in di.items():
        resGrade = round((v[0]*.3+v[1]*.3+v[2]*.4)+.4999) # i think this is the same as math.ceil?
        res[k] = resGrade
    return res

#6
def list_to_dict(li):
    res = {}
    for n in li:
        if not n in res:
            res[n] = 1
        else:
            res[n] += 1
    return res

#7
def dict_to_list(di):
    res = []
    for k,v in di.items():
        for _ in range(v):
            res.append(k)
    return res

#8
def most_cats(di):
    res = []
    high = 0
    for k,di2 in di.items():
        if "Cats" in di2:
            if di2["Cats"] > high:
                high = di2["Cats"]
                res.clear
            if di2["Cats"] == high:
                res.append(k)
    return res

#9
def oldest_cat(di):
    res = ""
    high = 0
    for k,di2 in di.items():
        for k2,age in di2.items():
            if age > high:
                high = age
                res = k2
    return res

#10
def owners_senior_cats(di):
    res = []
    high = 7
    for k,di2 in di.items():
        for k2,age in di2.items():
            if age >= high:
                res.append(k)
    return res

    