# from abc import ABCMeta, abstractmethod  # below 3.4 pythin version
from abc import ABC,abstractmethod
class Shape(ABC):   # class Shape(metaclass=ABCMeta): # below 3.4 pythin version
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7

    def printarea(self):
        return self.length * self.breadth

rect1=Rectangle()
print(rect1.printarea())