alf = "012345678"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    for n6 in alf:
                        word = n1+n2+n3+n4+n5+n6
                        flag = True
                        if n1 == "0":
                            flag = False
                        if int(n1) % 2 != 0:
                            flag = False
                        if n6 == "2" or n6 == "3":
                            flag = False
                        if word.count("1") < 2:
                            flag = False
                        if flag:
                            c = c + 1
print(c)
                        
                        