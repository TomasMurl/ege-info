def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

s = 5 * 1296 ** 2021 - 4 * 216 ** 2022 + 3 * 36 ** 2023 - 2 * 6 ** 2024 - 2025
s_36 = convert(s, 36)
c = 0
for i in s_36:
    if i % 2 == 0:
        c = c + 1
print(c)