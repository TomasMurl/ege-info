def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

s = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
s_27 = convert(s, 27)
c = 0
for i in s_27:
    if i > 9:
        c += 1
print(c)
# s_27 = [1, 4, 19, 23, 21, 7]
# [1, 1, 1]
# [19, 23, 21]
print(sum([1 for i in s_27 if i > 9]))