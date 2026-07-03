'''f1=open("info.txt","w")
count=f1.write("this")  #write method returns no.of.character it wrote
print(count)
list=[1,2,3,45]
for i in list:
    f1.write(str(i)+"\n")
c2=f1.writelines(str(list))  #writelines return none
print(c2)  
f1=open("info.txt","r")
#print(f1.read())
print(f1.readline())
#print(f1.readline())
print(f1.tell())
f1.seek(2)
print(f1.read())
print(f1.tell())
f1.close()'''


f1=open("info.txt","w")
f1.write("hi")
f1.flush()
f1=open("info.txt","r")
print(f1.read(1))