alf = '0123456789ABCDEFGHIJKL'

for x in alf:
    n1 = int(f'18{x}89957', 22)
    n2 = int(f'80{x}33', 22)
    n3 = int(f'521{x}6', 22)
    s = n1 + n2 + n3
    if s % 21 == 0:
        print(x, s // 21)
        break