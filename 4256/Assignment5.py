def star_m(n):
    row = [0 if i == 0 else 1 for i in range(n)]
    res = [row]
    row2 = [0 if row[i] == 1 else 1 for i in range(n)]
    res.append([row2] * (n - 1))
    return res

def star_d(n):
    res = {}
    zero = set()
    for i in range(1,n):
        zero.add(i)
        res[i] = {0}
    # dicts are unordered so 0 at the end is fine
    res[0] = zero
    return res
