def convert(n, b):
    r = []
    while n > 0:
        r.append(n%b)
        n = n // b
    return r[::-1]

for x in range(1, 3001):
    N = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    N_11 = convert(N, 11)
    if N_11.count(0) == 60:
        print(x)