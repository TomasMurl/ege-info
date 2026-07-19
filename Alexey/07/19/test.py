w = '1203120391232103193091231'
p = [1, 2, 3, 4]
for i in p:
    print(i)

s = 0
for i in w:
    s += int(i)

m = sum([int(i) for i in w])
print(m)