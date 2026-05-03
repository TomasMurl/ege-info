### Циклы

# for <название переменной> in <итерируемый объект>:
#     <code>

a = 'powderaw'
c = 0
for i in a:
    print(i + i)
    c = c + 1
print(c)

print('=============')

# range(end) - сгенерировать набор чисел (int) от 0 до end (не включительно)
# range(start, end)
# range(start, end, step)

# for i in range(5):
#     print('*****')
# for i in range(2, 10):
#     print(i)
for i in range(10, 0, -1):
    print(i)