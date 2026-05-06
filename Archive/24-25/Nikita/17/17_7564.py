file = open("17-409.txt")
m = []

max_m = -1000000000
for line in file:
    ch = int(line)
    m.append(ch)
    if ch > max_m and abs(ch) % 10 == 7 and 999 < abs(ch) < 10000:
        max_m = ch

c = 0
max_sum = -1000000
for i in range(len(m)-2):
    p = 0
    if abs(m[i]) % 10 == 7 and 999 < abs(m[i]) < 10000:
        p += 1
    if abs(m[i+1]) % 10 == 7 and 999 < abs(m[i+1]) < 10000:
        p += 1
    if abs(m[i+2]) % 10 == 7 and 999 < abs(m[i+2]) < 10000:
        p += 1
    summa = m[i] + m[i+1] + m[i+2]
    if summa > max_m and p >= 2:
        c += 1
        if summa > max_sum:
            max_sum = summa
print(c, max_sum)