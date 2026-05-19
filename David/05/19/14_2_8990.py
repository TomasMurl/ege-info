for x in '0123456789ABCDEFGHIJKL':
    s = int('12313' + x + '57', 22) + int('1' + x + '34561', 22)
    if s % 21 == 0:
        print(x, s // 21)