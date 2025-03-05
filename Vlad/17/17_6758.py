file = open('17-380.txt')
m = []
for line in file:
    m.append(int(line))

max_25 = -100000000
for i in m:
    if i > max_25 and str(i)[-2:] == "25":
        max_25 = i

c = 0
max_sum = -10000000
for i in range(len(m) - 2):
    p = 0
    if 999 < abs(m[i]) < 10000:
        p = p + 1
    if 999 < abs(m[i+1]) < 10000:
        p = p + 1
    if 999 < abs(m[i+2]) < 10000:
        p = p + 1
    summa = m[i] + m[i+1] + m[i+2]
    if p <= 2 and summa <= max_25:
        c = c + 1
        max_sum = max(summa, max_sum)
print(c, max_sum)