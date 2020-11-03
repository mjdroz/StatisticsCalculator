from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division
from square import square
from square_root import squareRoot

class calculator:
    result = 0

    def __init__(self):
        pass

    def add( self, a, b ):
        self.result = addition(a, b)
        return self.result

    def subtract( self, a, b ):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide( self, a, b ):
        self.result = division(a, b)
        return self.result

    def square( self, a ):
        self.result = square(a)
        return self.result

    def squareRoot( self, a ):
        self.result = squareRoot(a)
        return self.result