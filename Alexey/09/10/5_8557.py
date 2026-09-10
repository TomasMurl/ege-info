def convert(n, b) -> str:
    r = ''
    while n > 0:
        r += str(n%b)
        n = n // b
    return r[::-1]

m = []

for N in range(1, 100):
    N_3 = convert(N, 3)
    if N % 3 == 0:
        N_3 = N_3 + N_3[-2:] # N_3 + N_3[-2] + N_3[-1]
    else:
        sc = sum(int(i) for i in N_3)
        N_3 = N_3 + convert(sc * 3, 3)
    R = int(N_3, 3)
    if R > 208 and R % 2 != 0:
        m.append(R)

print(min(m))