print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = w and (not ((x <= y) <= (y == z)))
                if F == 1:
                    print(x, y, z, w, 1)

# zywx