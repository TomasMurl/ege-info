alf = sorted("ПРИВЫЧКА")
print(alf)
c = 0
a = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    word = n1 + n2 + n3 + n4 + n5
                    a += 1
                    if a % 5 == 0:
                        continue
                    c += 1
                    if sorted(word) == sorted("ВКПРЧ"):
                        print(c, word)
                        break
                    