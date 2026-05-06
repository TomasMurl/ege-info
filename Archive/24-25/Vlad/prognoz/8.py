alf = "АВЕНР"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    c += 1
                    word = n1+n2+n3+n4+n5
                    if c % 2 != 0 and word[0] != 'Н' and word.count("В") == 2:
                        print(c, word)
