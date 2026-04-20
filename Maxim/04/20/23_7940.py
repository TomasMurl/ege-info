def calc(s, e):
    if s < e or s == 24:
        return 0
    elif s == e:
        return 1
    else:
        return calc(s - 1, e) + calc(s - 6, e) + calc(s // 2, e)

print(calc(34, 29) * calc(29, 19) * calc(19, 6))
