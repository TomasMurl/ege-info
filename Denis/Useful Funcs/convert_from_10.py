def convert(n, b): # num base
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

a = convert(277, 5)
print(a)