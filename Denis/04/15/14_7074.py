for x in '0123456789AB':
    s = int(f'9A87{x}21', 12) + int(f'2{x}68', 14) - int(f'1{x}2F4', 16)
    if s % 3 == 0:
        print(x, s // 3)