file = open("17-339.txt")

m = []
min_p = 1000000
for line in file:
    ch = int(line)
    m.append(ch)
    if ch > 0 and ch < min_p and ch % 19 == 0:
        min_p = ch

c = 0
max_sum = 0
for i in range(len(m) - 1):
    sum_ij = m[i] + m[i+1]
    if sum_ij < min_p:
        c += 1
        if abs(sum_ij) > max_sum:
            max_sum = abs(sum_ij)

print(c, max_sum)