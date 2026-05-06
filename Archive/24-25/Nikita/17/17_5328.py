file = open("17-338.txt")

m = []
for line in file:
    ch = int(line)
    m.append(ch)

min_m = min(m)

c = 0
max_sum = -10000000
for i in range(len(m)-1):
    if m[i] % 117 == min_m or m[i+1] % 117 == min_m:
        c += 1
        if m[i] + m[i+1] > max_sum:
            max_sum = m[i] + m[i+1]
print(c, max_sum)