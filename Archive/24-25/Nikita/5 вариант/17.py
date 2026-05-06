file = open("17-411.txt")
m = []
for line in file:
    m.append(int(line))

def find_dels(n):
    dels = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i == i:
                dels.append(i)
            else:
                dels.append(i)
                dels.append(n // i)
    return dels

c = 0
min_sum = 10000000000000
for i in range(len(m) - 1):
    flag = True
    dels1 = find_dels(m[i])
    dels2 = find_dels(m[i + 1])
    for j in dels1:
        if j in dels2:
            flag = False
    if flag == True and m[i] % 2 != m[i + 1] % 2:
        c += 1
        min_sum = min( min_sum,  m[i] + m[i + 1] )
print(c, min_sum)