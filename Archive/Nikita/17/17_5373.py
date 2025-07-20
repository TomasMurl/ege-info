file = open("17-339.txt")

m = []
for line in file:
    m.append(int(line))

min_19 = 1000000
for i in m:
    if i > 0 and i % 19 == 0 and i < min_19:
        min_19 = i

c = 0
max_sum = -1000000
for i in range(len(m)-1):
    if (m[i] + m[i+1]) < min_19:
        c = c + 1
        if (m[i] + m[i+1]) > max_sum:
            max_sum = m[i] + m[i+1]

print(c, abs(max_sum))