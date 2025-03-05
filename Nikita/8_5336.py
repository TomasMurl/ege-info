alf = "012345678"
c = 0
for n1 in "12345678":
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    word = n1 + n2 + n3 + n4 + n5
                    if word.count("3") < 2 and word[0] not in "1357" and word[4] not in "18":
                        c += 1
print(c) 