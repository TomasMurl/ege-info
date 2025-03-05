file = open("17-379.txt")
m = []
for line in file:
    m.append(int(line))

max_15 = -1000000000
for i in m:
    if str(i)[-2:] == "15":
        max_15 = max(max_15, i)

c = 0
max_sum = -1000000000
for i in range(len(m) - 2):
    p = 0
    if 999 < m[i] < 10000:
        p = p + 1
    if 999 < m[i+1] < 10000:
        p = p + 1
    if 999 < m[i+2] < 10000:
        p = p + 1
    summa = m[i] + m[i+1] + m[i+2]
    if p == 1 and summa >= max_15:
        c = c + 1
        max_sum = max(summa, max_sum)
print(c, max_sum)
    