paths = []
def calc(c, e, l, d):
    if c > e or c == 12 or c == 20:
        return 0
    elif c == e:
        paths.append(d)
        return 1
    else:
        if l == 3:
            return calc(c + 1, e, 1, d + '1') + calc(c + 2, e, 2, d + '2')
        else:
            return calc(c + 1, e, 1, d + '1') + calc(c + 2, e, 2, d + '2') + calc(c * 3, e, 3, d + '3')

a = calc(2, 15, 0, '')
print('====== a ======')
for p in paths:
    if p[-1] == '3':
        print(p)
paths = []
b = calc(15, 30, 0, '')
print('====== b ======')
for p in paths:
    if p[0] == '3':
        print(p)
paths = []
c = calc(30, 38, 0, '')
print('====== c ======')
for p in paths:
    print(p)