file = open("17-338.txt")

m = []
for line in file:
    ch = int(line)
    m.append(ch)

min_ch = min(m)

c = 0
max_sum = 0
for i in range(len(m) - 1):
    if m[i] % 117 == min_ch or m[i+1] % 117 == min_ch:
        c += 1
        summa = m[i] + m[i+1]
        if summa > max_sum:
            max_sum = summa

print(c, max_sum)
