def calc(s, e):
    if s > e or s == 35:
        return 0
    if s == e:
        return 1
    return calc(s + 1, e) + calc(s + 2, e) + calc(s * 2, e)

print(calc(7, 13) * calc(13, 15) * calc(15, 51))
