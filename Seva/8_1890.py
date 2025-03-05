alf = "УЛЕЙ"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                word = n1 + n2 + n3 + n4
                flag = True
                if any(word.count(i) != 1 for i in word):
                    flag = False
                