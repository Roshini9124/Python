'''a={1,2,3,4,5}
print(a)
a.add(10)
print(a)
a.update(("h","i"))
print(a)
a.remove(1)
print(a)
a.discard(45)
print(a)
c={1:"emp1",2:"emp2"}
b=set(c.items())  #if .items() not used then only keys will be taken not values its by default
print(b)
'''
#a={3}
#b={3,4,5,3}
#print(a|b) #work  if both values are set  dont work  if atleast one is not set
c=[5,6,7,8]
d={1,2,3}
print(d.union(c))
#print(a.union(c))#work even if the values are diff union converts the iterable into same vice versa for other func

'''
print(a&b)
print(b.intersection(c))
print(a.difference(b)) #a-b 
print(a.symmetric_difference(b))#a^b
print(a.isdisjoint(b))
print(a.issubset(b))
print(len(b))
print(max(b))
print(min(b))
print(b.issuperset(a))'''

'''a=frozenset([1,2,3])
print(a)
a.add(5)'''


