def calc(c, e):
    if c > e:
        return 0
    elif c == e:
        return 1
    else:
        return calc(c + 1, e) + calc(c + 3, e) + calc(c * 4, e)

print(calc(1, 18))