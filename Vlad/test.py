# # .split(), .join(), map()
# a = "Привет, как дела"
# print( a.split(",") )

# mass = ["1", "3", "5"]
# # res = ''
# # for item in mass:
# #     res += item
# res = ", ".join(mass)
# print(res)

a = ["1", "3", "5"]
print( sum(list(map(int, a))) )