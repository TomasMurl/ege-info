a = open("17_21903.txt")
m = []
for line in a:
    m.append(int(line))

min_15 = 1000000
for i in m:
    if str(i)[-2:] == '15' and len(str(abs(i))) == 3:
        min_15 = min(min_15, i)
min_15 = min_15 ** 2

c = 0
min_pr = 1000000000000
for i in range(len(m) - 2):
    flag = True
    z = [m[i], m[i+1], m[i+2]]
    p = sum([1 for i in z if i > 0])
    if p == 1 or p == 2:
        flag = False
    pr = min(z) * max(z)
    if pr <= min_15:
        flag = False
    if flag:
        c += 1
        min_pr = min(min_pr, pr)
print(c, min_pr)

