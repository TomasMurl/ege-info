def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]

s = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
s_27 = convert(s, 27)

# c = [i for i in range(5) if i % 2 == 0]

# c = [i for i in s_27 if i > 9]

c = sum([1 for i in s_27 if i > 9])

# c = 0
# for i in s_27:
#     if i > 9:
#         c = c + 1
print(c)