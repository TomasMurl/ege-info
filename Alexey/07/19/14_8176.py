def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n = n // b
    return r[::-1]

for x in range(1, 2301):
    y = 7 ** 350 + 7 ** 150 - x
    y7 = convert(y,7)
    if y7.count("0") == 200:
        print(x)