alf = "АКЛОШ"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    word = n1+n2+n3+n4+n5
                    c += 1 # c = c + 1
                    if word == "ШКОЛА":
                        print(c)