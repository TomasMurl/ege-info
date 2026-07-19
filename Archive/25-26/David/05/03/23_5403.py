def calc(c, e, n):
    if c == e:
        if n % 2 == 0:
            return 0
        else:
            return 1
    elif c > e:
        return 0
    else:
        if c == 1:
            return calc(c + 2, e, n + 1) + calc(c * 2, e, n + 1)
        else:
            return calc(c + 2, e, n + 1) + calc(c * 2, e, n + 1) + calc(c ** 2, e, n + 1)

print(calc(1, 100, 0))