file = open('17-339.txt')
m = []
for line in file:
    m.append(int(line))

min_19 = 1000000000
for i in m:
    if i < min_19 and i % 19 == 0 and i > 0:
        min_19 = i

c = 0
max_sum = -100000000
for i in range(len(m) - 1):
    summa = m[i] + m[i+1]
    if summa < min_19:
        c = c + 1
        max_sum = max(summa, max_sum)

print(c, abs(max_sum))
