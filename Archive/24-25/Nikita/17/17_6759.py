f = open("17-381.txt")
m = []
max_m = -1000000
for l in f:
    ch = int(l)
    m.append(ch)
    if 999 < abs(ch) < 10000 and ch % 100 == 39 and ch > max_m:
        max_m = ch

c = 0
max_sum = -10000000
for i in range(len(m)-1):
    p = 0
    if 999 < abs(m[i]) < 10000:
        p += 1
    if 999 < abs(m[i+1]) < 10000:
        p += 1
    if p == 1 and (m[i]+m[i+1]) ** 2 <= max_m ** 2:
        c += 1
        if m[i]+m[i+1] > max_sum:
            max_sum = m[i]+m[i+1]
print(c, max_sum)