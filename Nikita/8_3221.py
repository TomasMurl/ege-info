alf = "ЖАЛЕЙ"
a = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    word = n1 + n2 + n3 + n4 + n5
                    if word.count("Й") < 2 and word[0] != "Й" and word[4] != "Й" and "ЙЕ" not in word and "ЕЙ" not in word:
                        a += 1
print(a)