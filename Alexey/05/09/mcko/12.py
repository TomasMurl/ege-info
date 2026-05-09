n = 38
n2 = bin(n)[2:].zfill(8)
print(n2)
n2 = n2.replace('0', '2')
n2 = n2.replace('1', '0')
n2 = n2.replace('2', '1')
print( bin(int(n2, 2) + 1)[2:] )