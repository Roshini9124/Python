class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

class Emp(Person):
    def __init__(self,name,age,empid,sal):
        super().__init__(name,age)
        self.empid=empid
        self.sal=sal      
    def display_person(self):
        super().display_person()
        print(f"Employee id:{self.empid}")
        print(f"Salary:{self.sal}")

class Dep(Emp):
    def __init__(self,name,age,id,sal,dept):
        super().__init__(name,age,id,sal)
        self.dept="Manager"
    def display_person(self):
        super().display_person()
        print(f"Department:{self.dept}")

e1=Dep("Joey",29,22,500000,"Actor")
e1.display_person()


    