def calc(c, e, d):
    if c > e:
        return 0
    elif c == e:
        if d:
            return 1
        else:
            return 0
    if c == 13 or c == 23:
        d = True
    return calc(c + 1, e, d) + calc(c + 5, e, d)+ calc(c * 2, e, d)

print(calc(5, 50, False))