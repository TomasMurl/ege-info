alf = "СЧИТАЙ"
c = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                word = n1 + n2 + n3 + n4
                if word.count("А") < 2:
                    c += 1
print(c)