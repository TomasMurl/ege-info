file = open('26-151.txt')
N, S = list(map(int, file.readline().split()))
m = [list(map(int, i.split())) for i in file.readlines()]
m = list([i[0], sum(i[1:4]), i[4]] for i in m)
m.sort(key=lambda x: (x[0]))
m.sort(key=lambda x: x[2], reverse=True)
m.sort(key=lambda x: x[1], reverse=True)
half_mark = m[S][1]
ans1, ans2 = {}, 0
for i in m:
    if i[1] > half_mark:
        ans1 = i
    elif i[1] == half_mark:
        ans2 += 1
    elif i[1] < half_mark:
        break
print(ans1[0], ans2)