def calc(start, end, l, pl):
    if start > end:
        return 0
    if start == end:
        return 1
    if l == pl and l != 0:
        if l == 1:
            return calc(start * 2, end, 2, l)
        else:
            return calc(start + 1, end, 1, l)
    return calc(start + 1, end, 1, l) + calc(start * 2, end, 2, l)

print(calc(1, 16, 0, 0))