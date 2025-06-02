def perevod(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

max_c_4 = 0
max_x = 0
for x in range(2, 2026):
    s = 5 ** 2025 + 5 ** 200 - x
    s_5 = perevod(s, 5)
    c_4 = s_5.count(4)
    if c_4 >= max_c_4:
        max_c_4 = c_4
        max_x = x 
print(max_x)

# x = 4 - 5
# x = 5 - 2
# x = 10 - 5
# x = 2000 max