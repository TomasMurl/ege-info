# file =
# m = []
# for line in file:
#     m.append(int(line))
m = [int(line) for line in open('17-476.txt')]

min_m = min(m)

c = 0
max_sum = 0
for i in range(len(m) - 1):
    if m[i] % 33 == min_m or m[i+1] % 33 == min_m:
        c += 1
        max_sum = max(m[i] + m[i+1], max_sum)
print(c, max_sum)
