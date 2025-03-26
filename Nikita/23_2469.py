def calc(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return calc(start + 1, end) + calc(start + 3, end) + calc(start * 2, end)

print(calc(1, 4) * calc(4, 9) * calc(9, 13))