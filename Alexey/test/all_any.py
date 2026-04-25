a = [1, 3, 5, 9]
print(all( i % 2 == 0 for i in a ))
print(any( i % 2 == 0 for i in a ))

print( list([x, y] for x in range(5) for y in range(5)) )