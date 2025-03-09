print("x y w F")
for x in range(2):
    for y in range(2):
        for w in range(2):
            F = (x <= y) and (w or (not w))
            if F == True:
                print(x, y, w, 1)
            if F == False:
                print(x, y, w, 0)