alf = '123456789ABCDEFGHI'

for x in alf:
    n1 = '98897' + x + '21'
    n2 = '2' + x + '923'
    n1 = int(n1, 19)
    n2 = int(n2, 19)
    s = n1 + n2
    if s % 18 == 0:
        print(x, s // 18)