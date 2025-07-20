def calc(start, end):
    if start == end:
        return 1
    if start > end or start == 25:
        return 0
    return calc(start + 1, end) + calc(start * 2, end) + calc(start * 3, end)

print(calc(2, 31))