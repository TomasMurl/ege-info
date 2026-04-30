def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

m = []
for N in range(1, 100000):
    N_3 = convert(N, 3)
    if N % 3 == 0:
        N_3 = N_3 + N_3[-2:]
    else:
        a = (N % 3 - 1) * 3
        N_3 = N_3 + convert(a, 3)
    R = int(N_3, 3)
    if R <= 200:
        m.append(R)
print(max(m))
# 199