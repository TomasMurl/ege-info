file = open("17-403.txt")
m = []
min_m = 1000000
for line in file:
    ch = int(line)
    m.append(ch)
    if ch < min_m:
        min_m = ch

c = 0
min_proiz = 1000000
for i in range(len(m) - 1):
    if (m[i] % 77) * (m[i+1] % 77) == min_m ** 2:
        c += 1
        proiz = m[i] * m[i+1]
        if proiz < min_proiz:
            min_proiz = proiz
print(c, min_proiz)