with open('17-381.txt') as f:
    m = list(map(int, f))
max_39 = max(x for x in m if (str(x)[-2:] == '39' and 999 < abs(x) < 10000))

cnt = 0
max_sum = -3000000
for i in range(len(m) - 1): # О
    a, b = m[i], m[i + 1]
    c = int(999 < abs(a) < 10000)
    d = int(999 < abs(b) < 10000)
    if c + d == 1 and ((a+b)**2 <= max_39**2):
        cnt += 1
        max_sum = max(max_sum, a + b)

print(cnt, max_sum)