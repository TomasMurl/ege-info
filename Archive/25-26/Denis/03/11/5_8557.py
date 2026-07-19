def convert(n, b): # num base
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

def sum(s):
    z = 0
    for i in s:
        z = z + int(i)
    return z

for N in range(1, 1000):
    N3 = convert(N, 3)
    if N % 3 == 0:
        N3 = N3 + N3[-2:]
    else:
        z = sum(N3)
        N3 = N3 + convert(z * 3, 3)
    R = int(N3, 3)
    if R % 2 != 0 and R > 208:
        print(R)