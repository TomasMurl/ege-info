# ## Задание 6. Индекс и элемент
# Дан список строк:
#
# ```python
# ["docker", "kubernetes", "terraform"]
# ```
# Выведи элементы в формате:
#
# ```python
# 0: docker
# 1: kubernetes
# 2: terraform
# ```

a = ["docker", "kubernetes", "terraform"]
# for i in a:
#     print(i)

for i in range(len(a)): # [0, 1, 2] = range(3)
    print(i, a[i])