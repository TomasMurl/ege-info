def calc(s, e):
    if s > e or s == 17:
        return 0
    if s == e:
        return 1
    return calc(s + 2, e) + calc(s + 3, e) + calc(s * 2, e)

print(calc(3, 10) * calc(10, 25))