def convert(n, b):
    r = []
    while n > 0:
        r.append(n%b)
        n = n // b
    return r[::-1]

n = 5*1296 ** 2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
n_36 = convert(n, 36)
c = 0
for x in n_36:
    if x % 2 == 0:
        c += 1
print(c)