def calc(c, e):
    if c < e:
        return 0
    elif c == e:
        return 1
    else:
        return calc(c - 3, e) + calc(c // 3, e)

print(calc(81, 27) * calc(27, 3))