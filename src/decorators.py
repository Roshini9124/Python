def dec(func):
    def wrapper(*args):
        print("Welcome user")
        ans=func(*args)
        
        print("Bye user")
        return ans
    return wrapper




@dec
def add(a,b):
    return (a+b)


res=add(5,4)
print(res)