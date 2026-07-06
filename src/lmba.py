'''res=lambda a,b:a+b

print(res(1,2))
print(res(3,4))'''



'''---------map()------------
def sq(n):
    return n*n
num=[1,2,3,34]


#res=map(lambda x:x*x,num)
res=map(sq,num)
#print(list(res))
for i in res:
    print(i)'''


'''def ans(word):
    l=len(word)
    return l
cities = ["Chennai", "Delhi", "Goa", "Mumbai"]
res=map(ans,cities)
#res=map(lambda x:len(x),cities)
print(list(res))'''

'''price = [100, 200, 300]
quantity = [2, 5, 3]

res=map(lambda a,b:a*b,price,quantity)
print(list(res))'''

'''numbers = [10, 15, 20, 25, 30]
res=filter(lambda x:x%2==1,numbers)
print(list(res))

names = ["Alice", "Bob", "Andrew", "John", "Anu"]
res=filter(lambda x:x[0].lower()=='a',names)
print(list(res))


emails = [
    "ram@gmail.com",
    "john@yahoo.com",
    "alice@gmail.com",
    "bob@hotmail.com"
]

res=filter(lambda x:x.endswith("@gmail.com")==False,emails)
print(list(res))


#reduce() → repeatedly combines elements until only one value remains.
#next() asks the generator for the next value.'''


def gen():
    for i in range(1,10):
        yield i
        print("hello")

g=gen()
