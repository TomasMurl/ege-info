def calc(c, e):
    if c < e:
        return 0
    elif c == e:
        return 1
    return calc(c - 1, e) + calc(c // 2, e)

result = calc( 40, 17) * calc( 17, 6)
print(result)