print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (z == (not y)) and ((not x) or y) and w
                if F == 1:
                    print(x,y,z,w,1)