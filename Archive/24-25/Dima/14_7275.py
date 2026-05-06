alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for p in range(9, 36):
    alf_p = alf[:p]
    for x in alf_p:
        for y in alf_p:
            for z in alf_p:
                for w in alf_p:
                    chislo1 = int(z+x+y+x+'8', p)
                    chislo2 = int(x+y+'517', p)
                    chislo3 = int(w+z+x+'62', p)
                    if chislo1 + chislo2 == chislo3:
                        print(int(x+y+z+w, p))