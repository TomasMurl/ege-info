def calc(c, e):
    if c > e or c == 35:
        return 0
    elif c == e:
        return 1
    else:
        return calc(c + 1, e) + calc(c + 2, e) + calc(c * 2, e)

print(calc(7, 13) * calc(13, 15) * calc(15, 51))