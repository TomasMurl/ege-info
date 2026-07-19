def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n = n // b
    return r[::-1]

m = []
for N in range(1, 1000):
    N_3 = convert(N, 3)
    if N % 2 == 0:
        N_3 = '2' + N_3 + convert(int(N_3[-1]) * 2, 3)
    else:
        N_3 = convert(int(N_3[0]) * 2, 3) + N_3 + '2'
    R = int(N_3, 3)
    if R > 100:
        m.append(R)
print(min(m))