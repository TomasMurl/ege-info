alf = "012345678"
c = 0
for n1 in "12345678":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    for n6 in alf:
                        for n7 in alf:
                            word = n1+n2+n3+n4+n5+n6+n7
                            if int(word[0]) % 2 == 0:
                                if int(word[-1]) % 3 != 0:
                                    if word.count("6") >= 1:
                                        c += 1
print(c)
