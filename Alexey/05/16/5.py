print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x) or y or w) and (y <= z)
                if F == 0:
                    print(x, y, z, w, 0)
