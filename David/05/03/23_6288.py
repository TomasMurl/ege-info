def calc(c, e, l):
    if c == e:
        return 1
    elif c > e:
        return 0
    else:
        if l == 1:
            return calc(c * 2, e, 2) + calc(c * 3, e, 2)
        elif l == 2:
            return calc(c + 1, e, 1) + calc(c + 3, e, 1)
        else:
            return calc(c + 1, e, 1) + calc(c + 3, e, 1) + calc(c * 2, e, 2) + calc(c * 3, e, 2)

print(calc(1, 9999, 0))