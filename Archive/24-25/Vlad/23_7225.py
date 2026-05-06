def calc(start, end, flag):
    if start == end:
        return 1
    if start > end:
        return 0
    if flag == 1:
        return calc(start + 3, end, 1) + calc(start * 7, end, 3)
    else:
        return calc(start + 3, end, 1) + calc(start * 5, end, 2) + calc(start * 7, end, 3)

print(calc(1, 1000, -1))