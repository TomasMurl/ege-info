def calc(c, e):
    if c > e or c == 10:
        return 0
    elif c == e:
        return 1
    else:
        return calc(c + 1, e) + calc(c + 2, e) + calc(c * 2, e)

print(calc(3, 7) * calc(7, 20))