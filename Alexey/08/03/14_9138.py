# 9138
# не верно, не знаю почему
def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

a = 5*1296**2021 - 4*216**2022 + 3 * 36 ** 2023 - 2*6 ** 2024 - 2025
a = convert(a,36)
n = 0
for item in a:
    if item % 2 == 0:
        n += 1
print(n)