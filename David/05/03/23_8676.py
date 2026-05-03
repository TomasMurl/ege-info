def calc(c, e):
    if c == e:
        return 1
    elif c < e or c == 36:
        return 0
    else:
        return calc(c - 3, e) + calc(c - 6, e) + calc(c // 2, e)

print(calc(86, 53) * calc(53, 12))