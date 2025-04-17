file = open("26-2024-osnova.txt")

N, rows_num, pls  = map(int, file.readline().split())
places = [list(map(int, line.split())) for line in file.readlines()]

places = sorted(places, key = lambda x: (x[1], x[0]))

placess = [[] for i in range(pls)]
for pl in places:
    placess[pl[1]-1].append(pl[0])

result = [0, 0]
for i in range(len(placess)):
    for j in range(len(placess[i])):
        if j == 0:
            c = placess[i][j] - 1
        else:
            c = placess[i][j] - placess[i][j-1] - 1
        if c > result[0]:
            result = [c - 1, placess[i][j] - 1]
    c = rows_num - placess[i][j] - 1
    if c > result[0]:
        result = [c, rows_num]
print(result)