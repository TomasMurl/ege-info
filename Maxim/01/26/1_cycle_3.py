## Задание 1. Индекс и длина слова
#
# Дан список строк:
#
# ```python
# ["aws", "docker", "kubernetes", "terraform"]
# ```
#
# Выведи индекс и длину каждого слова в формате:
#
# ```text
# 0: aws (3)
# 1: docker (6)
# 2: kubernetes (10)
# 3: terraform (9)
# ```

m = ["aws", "docker", "kubernetes", "terraform"]

for i in range(len(m)): # range(4) -> [0, 1, 2, 3]
    print(i, m[i], len(m[i]))
