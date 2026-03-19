file = open('26-174.txt')
N = int(file.readline())
m = []
for i in range(N):
    m.append(list(map(int, file.readline().split())))
m.sort(key=lambda x: (x[1], x[0]))
ma_le, dot = 0, 0
c_le = 0
for i in range(1, len(m)):
    if m[i][1] == m[i-1][1] and m[i][0] - m[i-1][0] in (0, 1):
        if m[i][0] - m[i-1][0] == 0:
            continue
        c_le += 1
        if c_le > ma_le:
            ma_le = c_le
            dot = m[i][1]
    else:
        c_le = 1
print(ma_le, dot)