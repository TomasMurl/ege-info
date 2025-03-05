file = open("17-409.txt")
m = []
max_7 = -1000000
for line in file:
    ch = int(line)
    m.append(ch)
    if 999 < abs(ch) < 10000 and abs(ch) % 10 == 7 and ch > max_7:
        max_7 = ch

c = 0
max_sum = -10000000
for i in range(len(m)-2):
    p = 0
    if 999 < abs(m[i]) < 10000 and abs(m[i]) % 10 == 7:
        p = p + 1
    if 999 < abs(m[i+1]) < 10000 and abs(m[i+1]) % 10 == 7:
        p = p + 1
    if 999 < abs(m[i+2]) < 10000 and abs(m[i+2]) % 10 == 7:
        p = p + 1
    summa = m[i] + m[i+1] + m[i+2]
    if p >= 2 and summa > max_7:
        c = c + 1
        if summa > max_sum:
            max_sum = summa
print(c, max_sum)