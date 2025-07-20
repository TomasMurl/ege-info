m = []
file = open('17-390.txt')
for line in file:
    m.append(int(line))

summa_151 = 0
colvo_151 = 0
for i in m:
    if str(i)[-3:] == "151":
        summa_151 += i
        colvo_151 += 1
ch_151 = summa_151 / colvo_151

c = 0
min_sum = 1000000000000
for i in range(len(m) - 2):
    troyka = [m[i], m[i+1], m[i+2]]
    p1 = 0
    c13 = 0
    c7 = 0
    p3 = 0
    for chislo in troyka:
        if len(str(abs(chislo))) == 4:
            p1 += 1
        if chislo % 13 == 0:
            c13 += 1
        if chislo % 7 == 0:
            c7 += 1
        if chislo > ch_151:
            p3 += 1
    if 0 < p1 < 3 and c13 > c7 and p3 == 3:
        c += 1
        min_sum = min(min_sum, sum(troyka))
print(c, min_sum)