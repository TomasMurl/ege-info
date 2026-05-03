def calc(c, e):
    if c == e:
        return 1
    elif c > e or c == 14:
        return 0
    else:
        return calc(c + 1, e) + calc(c * 2, e) + calc(c * 3, e)

print(calc(2, 39))