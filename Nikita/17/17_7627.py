file = open("17-410.txt")

m = [] # m.append(<a>)
for line in file:
    ch = int(line)
    m.append(ch)

min_m = 10000000
for i in m:
    if i < min_m:
        min_m = i

# max_m = -1000000
# for i in m:
#     if i > max_m:
#         max_m = i

# min_m = min(m)

c = 0
max_sum = 0
for i in range(len(m)-1):
    if m[i] % 16 == min_m or m[i+1] % 16 == min_m:
        c = c + 1
        if (m[i] + m[i+1]) > max_sum:
            max_sum = m[i] + m[i+1]
print(c, max_sum)