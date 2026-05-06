t = 3 * 16 ** 8 - 4 ** 5 + 3
n = 4
t_4 = ""

while t > 0:
    t_4 = str(t % n) + t_4
    t = t // n

print(t_4.count("3"))