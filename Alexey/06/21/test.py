def convert_old(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

print(convert_old(234, 16))
print(convert(234, 16))