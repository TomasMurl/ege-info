def perevod(n, osn):
    result = ''
    while n > 0:
        result = str(n % osn) + result
        n = n // osn
    return result

a = []
for N in range(1, 10000):
    N_3 = perevod(N, 3)
    if N % 3 == 0:
        N_3 = N_3 + N_3[-2:]
    else:
        r = (N % 3 - 1) * 3
        N_3 = N_3 + perevod(r, 3)
    R = int(N_3, 3)
    if R <= 200:
        a.append(R)
print(max(a))
# 199