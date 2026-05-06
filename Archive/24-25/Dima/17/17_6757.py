file = open("17-379.txt")
m = []
max_15 = 0
for line in file:
    ch = int(line)
    m.append(ch)
    if ch % 100 == 15 and ch > max_15:
        max_15 = ch

c = 0
max_sum = 0
for i in range(len(m)-2):
    p = 0
    if 999 < m[i] < 10000:
        p += 1
    if 999 < m[i+1] < 10000:
        p += 1
    if 999 < m[i+2] < 10000:
        p += 1
    summa = m[i] + m[i+1] + m[i+2]
    if p == 1 and summa >= max_15:
        c += 1
        if max_sum < summa:
            max_sum = summa

print(c, max_sum)