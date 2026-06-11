def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n = n // b
    return r[::-1]

print(convert(15, 2))