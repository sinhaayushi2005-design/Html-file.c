# Base class
class addition
    def add(self,a,b):
      return a+b

# Derived class 1
class subtraction(addition):
    def subtract(self,a,b):
       return a-b

# Derived class 2
class multiplication(subtraction):
    def multiply(self,a,b):
      return a*b

# Derived class 3
class calculator(multiplication):
    def divide(self,a,b):
      if b==0:
        return "cannot divide by zero"
      return a/b

    # main application
    calc=calculator




