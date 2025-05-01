def perevod(n, osn):
    res = ''
    while n > 0:
        res += str(n % osn)
        n = n // osn
    return res[::-1]

for N in range(1000000, 10000000):
    N_3 = perevod(N, 3)
    N_3 = N_3.replace("0", "a").replace("2", "0").replace("a", "2")
    R = abs(int(N_3, 3) - N)
    if R == 1824648:
        print(N)
        break