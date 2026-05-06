alf = "567"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    for n6 in alf:
                        for n7 in alf:
                            for n8 in alf:
                                for n9 in alf:
                                    for n10 in alf:
                                        for n11 in alf:
                                            for n12 in alf:
                                                flag = True
                                                word = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12
                                                if "55" in word:
                                                    flag = False
                                                if flag:
                                                    c += 1
print(c)