def dec(func):
    def wrapper(a,b):
        print("Welcome user")
        func(a,b)
        print("Bye user")
    return wrapper





def add(a,b):
    print(a+b)

res=dec(add)
res(5,4)