def calc(c, e):
    if c < e:
        return 0
    elif c == e:
        return 1
    else:
        return calc(c - 1, e) + calc(c // 2, e)

print(calc(50, 16) * calc(16, 5))