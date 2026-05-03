def calc(c, e):
    if c == e:
        return 1
    elif c < e:
        return 0
    else:
        return calc(c - 2, e) + calc(c // 2, e)

print(calc(28, 10) * calc(10, 1))