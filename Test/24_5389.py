file = open("24-215.txt")
s = file.readline()
import re
pattern = r"[ABC][123]{2}(?:[ABC][123]{2})*"

match = re.search(pattern, s)

if match:
    print(match.group())  # Выведет самую длинную найденную подстроку
else:
    print("Совпадений не найдено")
