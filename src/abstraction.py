from abc import ABC,abstractmethod
class Animal(ABC):
    #@abstractmethod
    def sound(self):
        pass
    def display(self):
        print("this is abstract class")
    def __init__(self):
        print("this is constructor")
class dog(Animal):

    def soundd(self):
       # self.__init__()
        print("Barks")


d=dog()
d.soundd()
d.display()