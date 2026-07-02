a=[1,2,3,8,4,7]
print("Original List:",a)
print("Maximum:",max(a))
print("Minimum:",min(a))
print("Sum:",sum(a))

'''print("Ascending order:")
a.sort()
print(a)
print("Desecnding order:" )
a.sort(reverse=True)
print(a)
print(a)'''

a.append("Hi")
print(a)
#a.extend((99,100))
#a.extend({4,5,6})
a.append({1,2,3})
a.append(('t','u','p','l','e'))
a.append({1:"emp1"})
print(f"Length:{len(a)}")
print(a[9][1])
a.insert(0,"hi")
print(a.pop(0))
a.remove(2)
print(a)
b=[1,2,3,4,5]
c=[1,2,3,4,6]
d=["Even" if i&1==0 else "Odd"  for i in c]
print(d)