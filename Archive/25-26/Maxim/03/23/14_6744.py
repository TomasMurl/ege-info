alf = '0123456789ABCDEFGHIJKLM'

for x in alf:
    n1 = int('7' + x + '38596', 23)
    n2 = int('14' + x + '36', 23)
    n3 = int('61' + x + '7', 23)
    s = n1 + n2 + n3
    if s % 22 == 0:
        print(x, s // 22)
        break