def dec2(func):
    def wrapper(*args):
        print("Welcome All")
        ans=func(*args)
        return ans+2
    return wrapper

def dec1(func):
    def wrapper(*args):
        print("Welcome")
        ans=func(*args)
        return ans*2
    return wrapper

@dec2
@dec1
def add(*args):
    return sum(args)



res=add(5,4,1)
print(res)