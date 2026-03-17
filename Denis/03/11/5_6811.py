def convert(n, b): # num base
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for N in range(1, 1000):
    N3 = convert(N, 3)
    if N % 3 == 0:
        N3 = '1' + N3 + '02'
    else:
        N3 = N3 + convert(N % 3 * 4, 3)
    R = int(N3, 3)
    if R < 199:
        print(R)