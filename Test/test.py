def awdawd(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs.values():
        print(f"kwargs - {i}")


u = [int(x) for x in range(1,4)]
awdawd(u,2,3,test = "awdaw",test1 = "awdadadwa")

