def calc(s, e):
    if s < e or s == 7:
        return 0
    if s == e:
        return 1
    return calc(s - 1, e) + calc(s - 4, e) + calc(s // 3, e)

print( calc(19, 13) * calc(13, 2) )