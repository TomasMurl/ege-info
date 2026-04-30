n=int(input())
m=[]
for i in range(n):
    m.append(int(input()))
p=int(input())
if (p>(len(m)-1)) or (p<(-len(m))):
    print("Элемента с таким индексом в этом массиве нет.")
else:
    print(m[p]**2)