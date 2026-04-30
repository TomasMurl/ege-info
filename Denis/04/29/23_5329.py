def calc(c, e):
    if c < e:
        return 0
    elif c == e:
        return 1
    else:
        return calc(c - 1, e) + calc(c // 2, e)

print( calc(30, 12) * calc(12, 1) )