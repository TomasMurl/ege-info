st = input("Введите строку - ")

if "@" in st or "#" in st or "$" in st:
    print("Содержит запрещенные символы!")
else:
    print("Все хорошо!")