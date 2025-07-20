m = []
file = open('17-432.txt')
for line in file:
    m.append(int(line))

sum_otric = sum([x for x in m if x < 0])

count = 0
max_sum = -1000000000000000
for i in range(len(m) - 2):
    a, b, c = m[i:i+3]
    min_t = min(a, b, c)
    max_t = max(a, b, c)
    if min_t * max_t > sum_otric:
        count += 1
        max_sum = max( max_sum, sum([a, b, c]) )
print(count, abs(max_sum))