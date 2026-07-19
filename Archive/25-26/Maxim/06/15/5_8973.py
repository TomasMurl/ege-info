def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

m = []
for N in range(19, 100):
    # N_2 = bin(N)[2:]
    N_2 = convert(N, 2)
    if N % 2 == 0:
        N_2 = '10' + N_2
    else:
        N_2 = '1' + N_2 + '01'
    R = int(N_2, 2) # Принимает строку состоящую из цифр ("1000110") и переводит в число
    m.append(R)
    print(R)
# print(min(m))