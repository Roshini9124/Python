'''class ageException(Exception):
    pass
    
num=12
try:
    if age<18:
        raise ageException ("Not eligible")
    else:
        print("Eligible")
except Exception as e:
    print(e)
else:
    print("No exception")
finally:
    print("Thank you")
'''

num=19
den=0
try:
    res=num/den
    print(res)
    print("THank you")
except ZeroDivisionError:
    print("Divide by zero error")
