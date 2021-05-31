import abc
import math

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculateArea():
        pass

class Arithmetics:
    def __add__(self, arg: Shape):
        return self.calculateArea() + arg.calculateArea()

    def __sub__(self, arg: Shape):
        firstOperand = self.calculateArea()
        secondOperand = arg.calculateArea()
        if firstOperand < secondOperand:
            raise ArithmeticError("Area1 less than Area2")
        else:
            return self.calculateArea() - arg.calculateArea()

    def __eq__(self, arg: Shape):
        return self.calculateArea() == arg.calculateArea() 

class Circle(Shape, Arithmetics):
    def __init__(self, radius,color='black'):
        self.radius = radius
        self.__color= color

    def calculateArea(self):
        return math.pi * self.radius ** 2
    
    def getColor(self):
        
        return self.__color

class Rectangle(Shape, Arithmetics):
    def __init__(self, a, b,color = 'black'):
        self.a = a
        self.b = b
        self.__color = color 

    def calculateArea(self):
        return self.a * self.b 

    def getColor(self):
        
        return self.__color

class Triangle(Shape, Arithmetics):
    def __init__(self, a, b,color ='black'):
        self.a = a
        self.b = b
        self.__color = color 

    def calculateArea(self):
        return self.a * self.b / 2
    
    def getColor(self):
        
        return self.__color

shapes = [Triangle(5, 2), Circle(1), Rectangle(2, 2)]
for shape in shapes:
    print(shape.calculateArea())

print(shapes[0].__sub__(shapes[2]))
print(shapes[2].__add__(shapes[0]))
t = Triangle(1,2)