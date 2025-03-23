def calc(start, end):
    if start == end:
        return 1
    if start < end or :
        return 0
    return calc(start - 2, end) + calc(start // 2, end)

print(calc(28, 10) * calc(10, 1))