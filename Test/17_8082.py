file = open('17-432.txt')

m = list(map(int, file.readlines()))
s = sum(i for i in m if i < 0)

c = 0
ma_s = 0
for i in range(len(m) - 2):
    ma = max(m[i], m[i+1], m[i+2])
    mi = min(m[i], m[i + 1], m[i + 2])
    p = ma * mi
    if p > s:
        c = c + 1
        ma_s = max(m[i] + m[i+1] + m[i+2], ma_s)
print(c, ma_s)