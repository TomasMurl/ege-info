def calc(start, end):
    if start > end or start == 8:
        return 0
    if start == end:
        return 1
    return calc(start + 1, end) + calc(start + 2, end) + calc(start * 2, end)

print(calc(3, 14) * calc(14, 18))