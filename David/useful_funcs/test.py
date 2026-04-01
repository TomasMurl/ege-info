def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

def convert2(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

print(convert(110, 14))
print(convert2(110, 14))