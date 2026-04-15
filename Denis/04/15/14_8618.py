for x in '0123456789ABCDEFGHIJKLMNOPQRS':
    s = int(f'923{x}874', 29) + int(f'524{x}6152', 29)
    if s % 28 == 0:
        print(x, s // 28)