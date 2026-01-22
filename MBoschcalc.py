import sys 
import re
class Calculator:
    """A class for tracking an object in the form of a number as it goes through mathematical operations

    Attributes:
        value: the float value of the number in the calculator
    """

    def __init__(self, value=0):
        """
        Return a new Calculator object.

        Usage:
            c = Calculator()
            c.result() # 0.0
            c = Calculator(1)
            c.result() # 1.0
        """
        self.number(value)
        self.value = float(value)

    def number(self, x):
        """
        Checks whether an input is valid:

        Usage: 
            c = Calculator()
            c = c.number(1) #No error issued
            c = c.number("a") #Raises TypeError
        """
        if not isinstance(x, (int, float)): 
            raise TypeError("Input must be a number.")

    def add(self, x):
        """
        Return the current value with a new value added, and update self.value

        Usage:
            c = Calculator(1)
            c = c.add(1).result() #2.0
        """
        self.number(x)
        self.value += x
        return self

    def sub(self, x):
        """
        Return the current value with a new value subtracted, and update self.value

        Usage:
            c = Calculator(1)
            c = c.sub(1).result() #0.0
        """
        self.number(x)
        self.value -= x
        return self

    def mul(self, x):
        """
        Return the current value with a new value multiplied, and update self.value

        Usage:
            c = Calculator(1)
            c = c.mul(4).result() #4.0
        """
        self.number(x)
        self.value *= x
        return self

    def div(self, x):
        """
        Return the current value divided through by a new value, and update self.value

        Usage:
            c = Calculator(4)
            c = c.div(2).result() #2.0
            c = Calculator(4)
            c = c.div(0).result() # Raises ZeroDivisionError
        """
        self.number(x)
        if x == 0: 
            raise ZeroDivisionError("Division by Zero is undefined")
        self.value /= x
        return self
        
    def clr(self):
        """
        Clear the value in the calculator and set it to zero
        Usage:
            c = Calculator(8)
            c = c.clr.result() #0.0
        """
        self.value = 0
        return self

    def result(self):
        """
        Return the numerical value stored in the calculator
        Usage:
            c = Calculator(1)
            c = c.result() #1.0
        """
        return self.value
    