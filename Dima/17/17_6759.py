file = open("17-381.txt")

m = []
m_39 = 0
for line in file:
    ch = int(line)
    m.append(ch)
    if (999 < ch < 10000 or -10000 < ch < -999) and ch % 100 == 39 and ch > m_39:
        m_39 = ch

c = 0
max_sum = -10000000
for i in range(len(m)-1):
    a = 0
    if 999 < m[i] < 10000 or -10000 < m[i] < -999:
        a += 1
    if 999 < m[i+1] < 10000 or -10000 < m[i+1] < -999:
        a += 1
    if a == 1:
        if (m[i]+m[i+1]) ** 2 <= m_39 ** 2:
            c += 1
            s = m[i] + m[i+1]
            if max_sum < s:
                max_sum = s

print(c,max_sum)


