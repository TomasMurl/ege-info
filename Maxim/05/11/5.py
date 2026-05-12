def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

min_R = 100000
for N in range(1, 100000):
    N_4 = convert(N, 4)
    s = 0
    for i in N_4:
        s = s + int(N_4)
    if s % 4 == 0:
        N_4 = N_4.replace('0', '5')
        N_4 = N_4.replace('3', '0')
        N_4 = N_4.replace('5', '3')
        N_4 = N_4 + '21'
    else:
        N_4 = N_4 + '22'
        N_4 = '11' + N_4[2:]
    R = int(N_4, 4)
    if R > 200 and R < min_R:
        print(N, R)
        min_R = R