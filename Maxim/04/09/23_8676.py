def calc(s, e):
    if s < e or s == 36:
        return 0
    if s == e:
        return 1
    return calc(s - 3, e) + calc(s - 6, e) + calc(s // 2, e)

print( calc(86, 53) * calc(53, 12) )