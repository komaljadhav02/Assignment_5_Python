# Challenge 2: Implement a Calculator Class

class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Addition :-", self.num1+self.num2)
    def subtract(self):
        if self.num1<self.num2:
            print( "Subtraction :- ",self.num2-self.num1)
        else:
            print("Subtraction :- ", self.num1-self.num2)
    def multiply(self):
        print("Multiplication :-" ,self.num1*self.num2)
    def divide(self):
        if self.num1<self.num2:
            print("Division :-", self.num2/self.num1)
        else:
            print("Division :-", self.num1/self.num2)
num1=int(input("Enter first number:- "))
num2=int(input("Enter second number:- "))
print(f"First number:- {num1}\nSecond number:- {num2}")
obj = Calculator(num1 , num2)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()