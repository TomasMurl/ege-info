def calc(start, end):
    if start == end:
        return 1
    if start > end or start == 21:
        return 0
    return calc(start + 1, end) + calc(start * 3, end) + calc(start * 4, end)

print( calc(2, 16) * calc(16, 60) )