file = open("17-411.txt")
m = []
for line in file:
    m.append(int(line))

max_3 = -10000000
for i in m:
    if i % 10 == 3 and i > max_3:
        max_3 = i

c = 0
min_sum = 1000000000
for i in range(len(m)-3):
    p = 0
    if m[i] % 10 == 2:
        p += 1
    if m[i+1] % 10 == 2:
        p += 1
    if m[i+2] % 10 == 2:
        p += 1
    if m[i+3] % 10 == 2:
        p += 1
    if p % 2 == 1 and m[i] < max_3 and m[i+1] < max_3 and m[i+2] < max_3 and m[i+3] < max_3:
        c += 1
        summa = m[i]+m[i+1]+m[i+2]+m[i+3]
        if summa < min_sum:
            min_sum = summa
print(c, min_sum)