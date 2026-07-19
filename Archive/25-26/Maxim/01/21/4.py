#Дана строка.
#Посчитай, сколько в ней гласных букв (a, e, i, o, u).
#Регистр можно не учитывать.

r = "aeiou"
stroka = "dad"
c = 0
for i in stroka:
    # if i == "e" or i == "i" or i == "o" or i == "u" or i == "a" or i == "j":
    #     c = c + 1
    if i in r:
        c = c + 1

print(c)