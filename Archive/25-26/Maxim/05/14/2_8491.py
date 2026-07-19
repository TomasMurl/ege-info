print('w x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or y) and (not (y == z)) and (not w)
                if F == 1:
                    print(w, x, y, z, 1)