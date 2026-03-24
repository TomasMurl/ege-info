# # 2
# while True:
#     s = input()
#     if s == '0':
#         break
#     print(len(s))

# # 4
# n = int(input())
# h = 12
# for i in range(h, n + h):
#     print(str(i % 24) + ':00')

# # 5
# r = ''
# while True:
#     s = input()
#     if s == '0':
#         break
#     if r == '':
#         r = s
#     else:
#         r = s + ' ' + r
# print(r)

# 3
s = 0
for i in range(1, 1000001):
    if i % 5 == 0:
        s = s + i
print(s)