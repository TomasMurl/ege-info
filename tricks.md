# 📘 Полезные трюки в Python для заданий

## 🔹 Работа со срезами

```python
a[:], a[::]
`````
Обычная форма записи, ничем не отличающаяся от простого вызова `a`

```python
a[:x]
````
Срез элементов до индекса `x` (x-й элемент **не включается**)

```python
a[x:]
````
Срез элементов начиная с индекса `x` (x-й элемент **включается**)

---

### 🔁 Обратные срезы

```python
a[-x:]
````
Возвращает элементы начиная с `-x` индекса (с конца)

---

### ⚙️ Общая форма

```python
a[a:b:c]
````
- `a` — начало  
- `b` — конец (не включается)  
- `c` — шаг  

---

## 🔹 Получение двоичной формы числа

```python
N_2 = bin(N)[2:]
````

- `N` — `int`  
- `N_2` — `str`  

Обрезаем префикс `'0b'` с помощью среза

---

## 🔹 Поиск максимума

### Через цикл

```python
m = 0
for i in arr:
    m = max(i, m)
````

⚠️ `m` нужно задать меньше минимального значения массива

---

### Быстрый способ

```python
m = max(arr)
````

---

### Поиск минимума

Просто меняем `max` → `min`

---

## 🔹 Сумма цифр числа

```python
s = sum(map(int, ch))
````

или

```python
s = sum(int(i) for i in ch)
````

- `ch` — строка (например `'1234'`)  
- `s` — число  

📌 Первый вариант короче, второй — через генератор

---

## 🔹 itertools (нужно в задании №8)

```python
from itertools import permutations, product, combinations
````

### Перестановки (без повторений)

```python
words = permutations('ABCDE', 3)
````

---

### Все комбинации (с повторениями)

```python
words = product('ABCDE', repeat=3)
````

---

### Комбинации с учетом порядка

```python
from itertools import combinations
`````

```python
words = combinations(range(10), 2)
````

- Формирует комбинации **с учётом порядка**
- Без повторений

Пример:
```python
(1, 2)
(1, 3)
````

---

### Важно!

```python
for w in words:
    w = ''.join(w)
````

Потому что:
```python
('A', 'B', 'C')
````
→ это кортеж, а не строка

---

## 🔹 Проверка соседних символов

```python
a = 'ABBCDE'

if all(x != y for x, y in zip(a, a[1:])):
    ...
````

✅ Условие выполняется, если **нет одинаковых соседних символов**

---

## 🔹 Перевод из 10-ичной системы (до основания 10)

```python
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r
````

- `n` — число  
- `b` — основание системы  

📌 Работает только для `b ≤ 10`

---

## 🔹 Перевод из 10-ичной системы (для любых оснований)

```python
def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n = n // b
    return r[::-1]
````

📌 Особенности:
- Работает для `b > 10`
- Возвращает **массив цифр**, а не строку

---

## 🔹 Работа с ip_address

```python
from ipaddress import ip_address
`````

```python
ip = ip_address('192.168.1.1')
````

---

## 🔹 Работа с ip_network

```python
from ipaddress import ip_network
````

```python
net = ip_network('192.168.1.0/24')
````

---

### Проверка принадлежности IP сети

```python
ip = ip_address('192.168.1.10')

if ip in net:
    ...
````

---

### Перебор всех IP в сети

```python
for ip in net:
    print(ip)
````

---

## 🔹 Генераторы (основа)

```python
gen = (i for i in range(5))
````

- Не создаёт список в памяти
- Выдаёт значения по одному

---

### Преобразование в список

```python
list(gen)
````

---

## 🔹 Генераторы с условиями

```python
gen = (i for i in range(10) if i % 2 == 0)
````

---

## 🔹 any() и all()

```python
any(i > 5 for i in arr)
````

→ True если **хотя бы один** элемент подходит

---

```python
all(i > 0 for i in arr)
````

→ True если **все** элементы подходят

---

## 🔹 enumerate (индекс + значение)

```python
for i, val in enumerate(arr):
    ...
````

---

## 🔹 zip (склейка списков)

```python
for a, b in zip(arr1, arr2):
    ...
````

---

## 🔹 распаковка списков

```python
a, b, c = [1, 2, 3]
````

---

## 🔹 игнорирование значений

```python
a, _, c = [1, 2, 3]
````

---

## 🔹 быстрый swap

```python
a, b = b, a
````

---

## 🔹 set для удаления дублей

```python
arr = list(set(arr))
````

---

## 🔹 проверка на уникальность

```python
len(arr) == len(set(arr))
````

---

## 🔹 сортировка

```python
arr.sort()
````

или

```python
sorted(arr)
````

---

## 🔹 сортировка по ключу

```python
arr.sort(key=lambda x: x[1])
````

---

## 🔹 переворот списка

```python
arr[::-1]
````