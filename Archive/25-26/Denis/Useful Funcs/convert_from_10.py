def convert(n, b): # num base
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

a = convert(131, 11)
print(a, type(a))

def convert(n, b): # num base
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

print(convert(131, 11))