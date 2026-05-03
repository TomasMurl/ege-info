def calc(c, e):
    if c == e:
        return 1
    elif c > e or c == 10:
        return 0
    else:
        return calc(c + 1, e) + calc(c + 2, e) + calc(c * 2, e)

print(calc(3, 7) * calc(7, 20))