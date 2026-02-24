from itertools import product, permutations

# product - комбинации с повторениями символов
# permutations - комбинации без повторений

# Любые комбинации всегда из двух параметров
# 1. Твой алфавит - какие символы ты можешь использовать
# 2. Длина комбинаций - длина слов

alf = "123"
words = product(alf, repeat=2)
# words = permutations(alf, 3)

for w in words:
    print(w)