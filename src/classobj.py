class Book:
    greet="Hello readers, Welcome to our library"
    @classmethod
    def changegreet(cls,name):
        cls.greet=f"Hello {name},Welcome to our library"
        print(cls.greet)
    def __init__(self,id,title,author,price,copy):
        self.id=id
        self.title=title
        self.author=author
        self.price=price
        self.copy=copy
    def display(self):
        print("Book Id:",self.id)
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Price:{self.price}")
        print(f"Copies:{self.copy}")
    def borrow(self):
        if self.copy>0:
            self.copy-=1
            print("Book borrowed successfully")
        else:
            print("No copies available")
    def returnbook(self):
        self.copy+=1
        print("Returned Succesfully")
    def updateprice(self,price):
        self.price=price

    def avail(self):
        if(self.copy>0):
            print("Available")
        else:
            print("Not Available")


b1=Book("001","Your time will come","Saranya umakanthan",250,12)
name=input("Enter your name:")
Book.changegreet(name)
#b1.display()
b1.avail()
b1.borrow()
#b1.borrow()
#b1.returnbook()
b1.updateprice(270)
b1.avail()
b1.display()