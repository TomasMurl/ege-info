file = open("17-381.txt")
m = []

max_39 = -10000000
for line in file:
    ch = int(line)
    m.append(ch)
    if 999 < abs(ch) < 10000 and str(ch)[-2:] == "39" and ch > max_39:
        max_39 = ch

c = 0
max_sum = -1000000
for i in range(len(m) - 1):
    p = 0
    if 999 < abs(m[i]) < 10000:
        p += 1
    if 999 < abs(m[i+1]) < 10000:
        p += 1
    summa = m[i] + m[i+1]
    if p == 1 and summa ** 2 <= max_39 ** 2:
        c += 1
        if summa > max_sum:
            max_sum = summa
    print(f"m[i] = {m[i]}, m[i+1] = {m[i+1]}, p={p}, \nsumma={summa}, max_39={max_39}\n")
print(c, max_sum, max_39)