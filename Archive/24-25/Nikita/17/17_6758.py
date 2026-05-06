file = open("17-380.txt")

m = []
for line in file:
    m.append(int(line))

max_25 = -1000000
for i in m:
    if str(i)[-1] == '5' and str(i)[-2] == '2' and i > max_25:
        max_25 = i

c = 0
max_sum = -10000000
for i in range(len(m)-2):
    p = 0
    m_1 = abs(m[i])
    m_1 = str(m_1)
    m_1 = len(m_1)
    if m_1 == 4:
        p += 1
    if len(str(abs(m[i+1]))) == 4:
        p += 1
    if len(str(abs(m[i+2]))) == 4:
        p += 1
    if p < 3 and (m[i] + m[i+1] + m[i+2]) <= max_25:
        c += 1
        if (m[i] + m[i+1] + m[i+2]) > max_sum:
            max_sum = (m[i] + m[i+1] + m[i+2])
print(c, max_sum)