def sym_diff(s, t):
    res = s.difference(t)
    return res.union(t.difference(s))

print(sym_diff({1,4,5},{2,4}))


