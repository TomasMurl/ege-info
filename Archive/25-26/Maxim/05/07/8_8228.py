def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

c = 0
for N in range(531441):
    N_3 = convert(N, 3)
    n = 0
    for i in range(len(N_3) - 1):
        if int(N_3[i]) % 2 != int(N_3[i + 1]) % 2:
            n += 1
    if n <= 3:
        continue
    s = 0
    for i in N_3:
        s += int(i)
    if N % s != 0:
        continue
    c += 1
print(c)