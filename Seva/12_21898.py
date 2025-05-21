def red(s):
    while '19' in s or '399' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '399' in s:
            s = s.replace('399', '91', 1)
        if '999' in s:
            s = s.replace('999', '3', 1)
    return s

for n in range(3, 10001):
    s = "1" + "9" * n
    result = red(s)
    sc = sum([int(j) for j in result])
    if sc == 33:
        print(n)
        break