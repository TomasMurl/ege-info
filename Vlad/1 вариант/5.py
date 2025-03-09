def perevod(n, osn):
    otv = ''
    while n > 0:
        otv = str(n % osn) + otv
        n = n // osn
    return otv
N_list = []
for N in range(1, 100):
    N_3 = perevod(N, 3) # str
    N_3 = N_3 + perevod(N_3.count("2"), 3)
    N_3 = N_3 + perevod(N_3.count("1"), 3)
    N_3 = N_3 + perevod(N_3.count("0"), 3)
    R = int(N_3, 3)
    if R < 1000:
        N_list.append(N)
print(max(N_list))