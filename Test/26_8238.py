file = open('26-172.txt')
N = int(file.readline())
m = [list(map(int, i.split())) for i in file.readlines()]
times = []
c = 1
for i in m:
    times.append([i[0], 0, c])
    times.append([i[1], 1, c])
    c += 1
times.sort(key=lambda x: x[0])
places = [0] * N
i, j = 0, N - 1
l, c_sh = 0, 0
for d in times:
    if d[2] not in places:
        if d[1] == 0:
            places[i] = d[2]
            i += 1
        else:
            places[j] = d[2]
            j -= 1
        l = d[2]
print(l, i)