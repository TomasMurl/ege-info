def calc(c, e):
    if c < e or c == 7:
        return 0
    elif c == e:
        return 1
    else:
        return calc(c - 1, e) + calc(c - 4, e) + calc(c // 3, e)

print(calc(19, 13) * calc(13, 2))