file = open("17-411.txt")
m = []
for line in file:
    m.append(int(line))

max_3 = -100000000
for i in m:
    if str(i)[-1] == "3":
        max_3 = max(max_3, i)

c = 0
min_sum = 1000000000
for i in range(len(m) - 3):
    p = 0
    if str(m[i])[-1] == "2":
        p += 1
    if str(m[i+1])[-1] == "2":
        p += 1
    if str(m[i+2])[-1] == "2":
        p += 1
    if str(m[i+3])[-1] == "2":
        p += 1
    summa = m[i] + m[i+1] + m[i+2] + m[i+3]
    if p % 2 != 0 and m[i] < max_3 and m[i+1] < max_3 and m[i+2] < max_3 and m[i+3] < max_3:
        c += 1
        min_sum = min(min_sum, summa)
print(c, min_sum)