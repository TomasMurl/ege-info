def calc(start, end, flag):
    if start == end:
        return 1
    if str(start)[-1] == '0':
        return 0
    if flag == 1:
        return calc(start + 2, end, 2) + calc(start * 3, end, 3)
    else:
        if start > end:
            if start - 1 == end:
                return 1
            else:
                return 0
        return calc(start - 1, end, 1) + calc(start + 2, end, 2) + calc(start * 3, end, 3)

print( calc(5, 32, -1) * calc(32, 62, -1) )

# UPD: Глянуть позже