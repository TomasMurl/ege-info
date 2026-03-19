file = open('26-170.txt')
N = int(file.readline())
m = [list(map(int, i.split())) for i in file.readlines()]
m.sort(key=lambda x: (x[0], x[1]))
st, max_t = 0, [0, set()]
for i in range(1, len(m)):
    if m[i][0] == m[i-1][0]:
        if m[i][1] == m[i-1][1]:
            continue
        elif m[i][1] - m[i - 1][1] == 2:
            st += 1
            if st > max_t[0]:
                max_t = [st, {m[i][0]}]
            elif st == max_t[0]:
                max_t[1].add(m[i][0])
        else:
            st = 1
    else:
        st = 1
print(max_t[0], min(max_t[1]))
