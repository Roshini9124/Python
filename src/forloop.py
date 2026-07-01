a=[1,2,3,45,7]

'''for i in range(0,len(a)):
    print(i,a[i])'''

'''for i,j in enumerate(a):
    print(i,j)'''
'''for i in range(len(a)-1,-1,-1):
    print(i,a[i])
'''
'''for i in reversed(a):
    if i==3:
        print(i)
        break

else:
    print("no break")'''

'''for i in range(-1,-(len(a)+1),-1):
    print(i,a[i])'''


'''for i in range(1,6):
    num=6*i
    print(num)'''


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()