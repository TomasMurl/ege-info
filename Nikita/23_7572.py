def calc(start, end):
    if start == end:
        return 1
    if start < end:
        return 0
    return calc(start - 2, end) + calc(start // 2, end)

print(calc(32, 14) * calc(14, 1))