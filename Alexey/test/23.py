g = [list(map(float, s.split())) for s in open('23-1.txt')]
d = [float('inf')] * 1001
d[1] = 0
for _ in range(200):
    for l, m, w in g:
        l, m = int(l), int(m)
        d[m] = min(d[m], d[l] + w)
print(d[100])