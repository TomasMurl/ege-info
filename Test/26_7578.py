file = open('26-153.txt')
N = int(file.readline())
m = [list(map(int, i.split())) for i in file.readlines()]

mean = sum(list([i[1] for i in m])) / N
l = [0, []]
m.sort(key=lambda x: x[0])
c_art, c_sold = 0, 0
for i in m:
    if i[1] > mean:
        if i[0] == c_art:
            if i[2]:
                c_sold += 1
                if c_sold > l[0]:
                    l = [c_sold, [i]]
                elif c_sold == l[0]:
                    l[1].append(i)
        else:
            c_art = i[0]
            c_sold = i[2]
    else:
        continue
print(l, sum([1 for i in m if m[0] == 59069 and m[2] == 0]))