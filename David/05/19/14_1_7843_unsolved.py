def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

for x in range(1, 10000000):
    s = 5*9**22 + 3*9**12 + 2*81**5 + 5*729**2 + 30 - x
    s_9 = convert(s, 9)
    if s_9.count(8) > s_9.count(0):
        print(x)
        break