print("w x y z F")
for w in range(2): # range(2) = [0, 1]
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))
                if F == 1:
                    print(w,x,y,z,1)