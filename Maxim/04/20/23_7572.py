def calc(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    return calc(s - 2, e) + calc(s // 2, e)

print(calc(32, 14) * calc(14, 1))