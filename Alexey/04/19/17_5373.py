with open('17-339.txt') as f:
    m = list(map(int, f.readlines()))

min_19 = min(x for x in m if x % 19 == 0 and x > 0)

c = 0
max_sum = -1000000
for i in range(len(m) - 1):
    a, b = m[i], m[i+1]
    s = a + b
    if s < min_19:
        c += 1
        max_sum = max(s, max_sum)
print(c, abs(max_sum))