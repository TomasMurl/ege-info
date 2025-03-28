def calc(start, end):
    if start < 13:
        return 0
    if start == end:
        return 1
    return calc(start - 3, end) + calc(start // 3, end) + calc(start - 2, end)

print( calc(43, 21) * calc(21, 15) * calc(15, 13) )