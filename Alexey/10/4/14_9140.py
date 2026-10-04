def convert(n,b):
    r = ''
    while n > 0:
        r += str(n%b)
        n = n // b
    return r[::-1]

max_null = 1
for x in range(1,2031):
    N = 5**150 + 5**100 - x
    N_5 = convert(N,5)
    if N_5.count("0") >= max_null:
        max_null = N_5.count("0")
        print(x)