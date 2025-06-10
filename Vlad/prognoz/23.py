def calc(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    return calc(start - 3, end) + calc(start // 3, end)

print(calc(81, 27) * calc(27, 3))