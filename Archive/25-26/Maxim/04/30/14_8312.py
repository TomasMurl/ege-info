alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for p in range(18, 36):
    a = alf[:p+1]
    s = int('22A12E', p) + int('2F1391', p) - int('1H05D0', p)
    if s % 19 == 0:
        print(p, s // 19)
        break
# 819869