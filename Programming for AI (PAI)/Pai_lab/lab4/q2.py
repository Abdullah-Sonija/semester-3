from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,len,wid):
        self.length=len
        self.width=wid
    
    def area(self):
        area= self.length*self.width
        return area
    def print(self):
        print(f"The area: {self.area()}")
    
class Triangle(Shape):
    def __init__(self,base,prep):
        self.base=base
        self.prependicular=prep
    
    def area(self):
        area= self.base*self.prependicular*.5
        return area
    def print(self):
        print(f"The area: {self.area()}")

class Square(Shape):
    def __init__(self,len):
        self.length=len
    
    def area(self):
        area=self.length**2
        return area
    
    def print(self):
        print(f"The area: {self.area()}")

s=Square(5)
t=Triangle(5,3)
r=Rectangle(5,3)

s.print()
t.print()
r.print()