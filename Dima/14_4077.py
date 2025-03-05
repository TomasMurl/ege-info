t = 6 * 343 ** 1156 - 5 * 49 ** 1147 + 4 * 7 ** 1153 - 875
n = 7
t_7 = ""
while t > 0:
    t_7 = str(t % n) + t_7
    t = t // n

summ = 0
for i in t_7:
    summ += int(i)
print(summ)