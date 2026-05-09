for x in '0123456789AB':
    s = int(f'154{x}3', 12) + int(f'1{x}365', 12)
    if s % 13 == 0:
        print(x, s // 13)