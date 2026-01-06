def high_grades(di):
    res = {}
    for name in di:
        resGrades = 0
        for num in di[name]:
            if num >= 90:
                resGrades += 1
        res[name] = resGrades
    return res