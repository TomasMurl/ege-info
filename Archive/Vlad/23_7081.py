def calc(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return calc(start + 2, end) + calc(start ** 2, end) + calc(start ** 3, end)

print( calc(10, 1000) )