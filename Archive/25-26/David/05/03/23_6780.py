def calc(c, e):
    if c == e:
        return 1
    elif c < e or c == 7:
        return 0
    else:
        return calc(c - 1, e) + calc(c - 3, e) + calc(c // 2, e)

print(calc(19, 10) * calc(10, 3))