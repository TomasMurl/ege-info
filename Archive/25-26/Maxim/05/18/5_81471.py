def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for N in range(1, 100):
    N_3 = convert(N, 3)
    if N % 3 == 0:
        N_3 = '1' + N_3 + '02'
    else:
        N_3 = convert(N % 3 * 4, 3) + N_3
    R = int(N_3, 3)
    if R > 135:
        print(N)
        break