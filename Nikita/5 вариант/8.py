alf = "012345678"
c = 0
for n1 in "12345678":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    for n6 in alf:
                        flag = True
                        word = n1 + n2 + n3 + n4 + n5 + n6
                        if word[0] not in "2468":
                            flag = False
                        if word[-1] in "23":
                            flag = False
                        if word.count("1") < 2:
                            flag = False
                        if flag == True:
                            c += 1
print(c)