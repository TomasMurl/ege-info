def perevod(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

a = [10, 20, 30, 40, 50]
print(a[:2])