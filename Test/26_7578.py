file = open('26-153.txt')
N = int(file.readline())
m = [list(map(int, i.split())) for i in file.readlines()]

mean = sum(i[1] for i in m) / N
l = [0, []]
m.sort(key=lambda x: x[0])
c_art, c_sold = 0, 0
for i in m:
    if i[1] > mean:
        if i[0] == c_art:
            if i[2] == 0:
                c_sold += 1
                if c_sold > l[0]:
                    l = [c_sold, [[i[0], i[1]]]]
                elif c_sold == l[0]:
                    l[1].append([i[0], i[1]])
        else:
            c_art = i[0]
            c_sold = i[2]

print(l)
s = {}
for i in [45510, 59069]:
    su = sum(1 for j in m if j[0] == i and j[2] == 1)
    s[i] = [su, su * 802]
print(s)