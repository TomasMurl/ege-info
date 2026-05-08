def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

R_min = 100000000000
for N in range(166, 1000):
    N_3 = convert(N, 3)
    s = 0
    for i in N_3:
        s += int(i)
    if s % 9 == 0:
        N_3 = N_3 + '2'
    else:
        N_3 = N_3 + convert(s % 9, 3)
    R = int(N_3, 3)
    if R < R_min:
        R_min = R
print(R_min)
