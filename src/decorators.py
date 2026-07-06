def dec(func):
    def wrapper(a,b):
        print("Welcome user")
        func(a,b)
        print("Bye user")
    return wrapper




@dec
def add(a,b):
    print(a+b)

add(5,4)