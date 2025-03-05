file = open("17-380.txt")

m = []
max_25 = -1000000
for line in file:
    ch = int(line)
    m.append(ch)
    if ch % 100 == 25 and ch > max_25:
        max_25 = ch

c = 0
max_sum = -100000
for i in range(len(m)-2):
    p = 0
    if 999 < m[i] < 10000 or -10000 < m[i] < -999:
        p = p + 1
    if 999 < m[i+1] < 10000 or -10000 < m[i+1] < -999:
        p = p + 1
    if 999 < m[i+2] < 10000 or -10000 < m[i+2] < -999:
        p = p + 1
    summa = m[i] + m[i+1] + m[i+2]
    if p <= 2 and summa <= max_25:
        c = c + 1
        if summa > max_sum:
            max_sum = summa

print(c, max_sum)