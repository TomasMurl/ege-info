t = 4 ** 512 + 8 ** 512 - 2 ** 128 - 250
n = 2
t_2 = ""

while t > 0:
    t_2 = str(t % n) + t_2
    t = t // 2

print(t_2.count("0"))