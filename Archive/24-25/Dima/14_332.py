t = 4 ** 2014 + 2 ** 2015 - 8
n = 2
t_2 = ""

while t > 0:
    t_2 = str(t % n) + t_2
    t = t // n

print(t_2.count("1"))