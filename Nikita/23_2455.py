def calc(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return calc(start + 1, end) + calc(start * 3, end)

print(calc(1, 22) * calc(22, 70))