for n in range(4, 10000):
    s = '5' + '7' * n
    while '577' in s or '677' in s or '657' in s:
        if '577' in s:
            s = s.replace('577', '76', 1)
        if '677' in s:
            s = s.replace('677', '75', 1)
        if '657' in s:
            s = s.replace('657', '56', 1)
    sc = sum(map(int, s))
    if sc == 76:
        print(n)