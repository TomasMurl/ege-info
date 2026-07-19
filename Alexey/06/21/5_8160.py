def convert(n, b):
    r = ''
    print(n, r)
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

for N in range(1, 100):
    N_3 = convert(N, 3)
    if N % 3 == 0:
        N_3 = N_3 + N_3[-2:]
    else:
        F = convert(N % 3 * 3, 3)
        N_3 = N_3 + F
    R = int(N_3, 3)
    if R <= 150:
        print(N)