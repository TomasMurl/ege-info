# 1. перевод 10 -> x
# 2. перевод x -> 10

def convert(n, b):
    r = ''
    while n > 0:
        r += str(n%b)
        n = n // b
    return r[::-1]

def convert2(n, b):
    r = []
    while n > 0:
        r.append(n%b)
        n = n // b
    return r[::-1]

for x in range(1, 2031):
    N = 7 ** 170 + 7 ** 100 - x
    N_7 = convert2(N, 7)
    if N_7.count(0) == 70:
        print(x)