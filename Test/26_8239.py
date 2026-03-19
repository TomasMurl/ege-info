file = open('26-173.txt')
k = int(file.readline())
N = int(file.readline())

m = [list(map(int, i.split())) for i in file.readlines()]
specs = [0] * k
m.sort(key=lambda x: (x[0], x[1]))
t, l = 0, 0
for i in m:
    if 0 in specs:
        for j in range(k):
            if specs[j] == 0:
                specs[j] = i[1]
                break
        t += 1
    else:
        for j in range(k):
            if specs[j] < i[0]:
                specs[j] = i[1]
                t += 1
                l = j
                break
print(t, l)