m = [int(line) for line in open('17-475.txt')]

max_m = max(x for x in m if 999 < abs(x) < 10000 and str(x)[-1] == '3')

d = 0
max_sum = -1_000_000
for i in range(len(m) - 2):
    a, b, c = m[i], m[i+1], m[i+2]
    sc = a + b + c
    p = 0
    for j in [a, b, c]:
        if str(j)[-1] == '3' and 999 < abs(j) < 10000:
            p += 1
    if p == 2 and sc > max_m:
        max_sum = max(sc, max_sum)
        d += 1
print(d, max_sum)
