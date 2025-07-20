alf = "АНДРЕЙ"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    for n6 in alf:
                        for n7 in alf:
                            word = n1+n2+n3+n4+n5+n6+n7
                            flag = True
                            if word.count("А") != 1:
                                flag = False
                            if word.count("Й") != 1:
                                flag = False
                            if n1 == "Й":
                                flag = False
                            if flag == True:
                                c += 1
print(c)