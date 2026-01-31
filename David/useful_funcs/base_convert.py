def perevod(n, osn):
    result = ''
    while n > 0:
        result = str(n % osn) + result
        n = n // osn
    return result

a = perevod(21312, 7)
print(a)