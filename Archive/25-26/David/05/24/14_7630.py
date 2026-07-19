def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

x = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 5 * 25**4 - 2025

print(convert(x, 25).count(0))