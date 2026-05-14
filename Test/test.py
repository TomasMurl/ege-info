N = int(input())

k = []
r = [[], [], []]
for i in range(N):
    k.append(input())

c = 0
for i in range(N):
    col = input()
    if col == 'зеленый':
        c = 1
    elif col == 'коричневый':
        c = 2
    r[c].append(k[i])

print(r[0])
print(r[1])
print(r[2])