def perevod(n, osn):
    res = ''
    while n > 0:
        res += str(n % osn)
        n //= osn
    return res[::-1]

min_m = 1000
for N in range(1, 1000):
    N1 = perevod(N, 3)
    if N % 2 == 0:
        N1 = '2' + N1 + perevod(int(N1[-1]) * 2, 3)
    else:
        N1 = perevod(int(N1[0]) * 2, 3) + N1 + '2'
    R = int(N1, 3)
    if R > 100:
        min_m = min(min_m, R)
print(min_m)