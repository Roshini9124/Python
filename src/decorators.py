def dec(func):
    def wrapper(*args):
        print("Welcome user")
        ans=func(*args)
        
        print("Bye user")
        return ans
    return wrapper




@dec
def add(*args):
    return sum(args)


res=add(5,4)
print(res)