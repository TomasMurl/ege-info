s = input("Введите один символ - ")

glas = "aeiou"
# if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
if s in glas:
    print("Гласная!")
else:
    print("Согласная!")