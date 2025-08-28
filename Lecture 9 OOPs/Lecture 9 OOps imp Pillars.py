#1) Abstarction - hiding unnecessary details from user
"""
class Car:
    def __init__(self):         
        self.acc=False          
        self.brk=False          
        self.cluth=False        

    def start(self):
        self.clutch= True       #unnecessary
        self.acc=True           #details which we hid from user
        print(" car started..")

car1 = Car()
car1.start()
"""

#2) Encapsulation - wrapping data an related fns into a single unit

#3) del - keyword
"""

class Student:
    def __init__(self,name):
        self.name=name
s1= Student("hitesh")
print(s1.name)
del s1.name
print(s1.name)

"""

#4) Private attributes
"""
class Student:
    def __init__(self,name):
        self.name=name
s1= Student("hitesh")
print(s1.name) #name = public attribute, can e used outside the scope of class
"""


"""
class Acc:
    def __init__(self,acno,acpw):
        self.acno=acno 
        self.__acpw=acpw    # we made acpw atrr pvt by typing __ behind it,but can be acccesses inside class only
    def resetpw(self):
        print(self.__acpw)

A1= Acc(12345678,"password")

print(A1.acno)
print(A1.resetpw())

"""

#5) private methods
"""
class Person:
    __name="anonymous"
    def __hello(self):    # private method by typing '__' behind the function
        print("hello",self.__name)
    def welcome(self):
        self.__hello()
P1=Person()
#P1.hello() #will give erroe beacuse the method is not accessible from outside the class
P1.welcome()
"""

#6) Inheritance
"""
class Car:                          #parent class
    color="black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota_car(Car):              # child class
    def __init__(self,model):
        self.model=model

car1=Toyota_car("fortuner")
car2=Toyota_car("hyrer")
print(car1.model)
print(car1.start())
print(car1.color)

"""

# Multi level inheritance
"""
class Car:                          #parent class
    color="black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota_car(Car):              # child class / parent class
    def __init__(self,model):
        self.model=model


class Fortuner(Toyota_car):         #child class  inheriting properties of Toyota_car and Car classes
    def __init__(self, type):
        self.type=type
    

car1=Fortuner("Diesel")

print(car1.start())
print(car1.color,car1.type)

"""

# Multiple inheritance

"""
class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):           # C inheriting properties of class A and B both
    varC="Welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
"""


# super() method
"""
class Car:    
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota_car(Car):             
    def __init__(self,model,type):
        self.model=model
        super().__init__(type)   #super constructor calling constructor in super class
        super().start()

car1=Toyota_car("innova","electric")
print(car1.type)
"""

# class method

"""

class Person:
    name= "anonymous"

   # def changename(self,name):
        # Person.name=name -> one method to change class attr.
        # self.__class__.name= name # second method (instance method)
    @classmethod
    def changename(cls, name):
        cls.name=name   #class method
p1=Person()
p1.changename("rahul kumar")
print(p1.name)

print(Person.name)
"""
#@property constructor
"""
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property    #makes the calculn dependent on obj attr
    def calcperc(self): #returns an object/ behaves as an obj
        return str((self.phy+self.chem+self.math)/3)+"%" 

stu1=Student(98,97,99)
stu1.phy=86 
print(stu1.calcperc)

"""

#Polymorphism - diff meaning of operator acc to context
"""
print(12) # + operator performs addition
print("Hello"+"World") # + operator performs concatenation
print([1,2,3]+[4,5,6]) # + operator performs merging of lists
"""

# we are creating a class representing complex numbers and operators to work on them

#1) without defining operator
"""
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def shownum(self):
        print(self.real,"i +",self.img,"j")

    def add(self,n2):
        newreal=self.real+n2.real
        newimg=self.img+n2.img
        return Complex(newreal,newimg)

num1 = Complex(1,3)
num1.shownum()
num2 = Complex(5,6)
num2.shownum()

num3 = num1.add(num2)
num3.shownum()
"""
#2) defining operator using dunder function

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def shownum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,n2):
        newreal=self.real+n2.real
        newimg=self.img+n2.img
        return Complex(newreal,newimg)
    
    def __sub__(self,n2):
        newreal=self.real+n2.real
        newimg=self.img-n2.img
        return Complex(newreal,newimg)

num1 = Complex(1,3)
num1.shownum()
num2 = Complex(5,6)
num2.shownum()

num3 = num1 + num2
num3.shownum()
num4 = num2-num1
num4.shownum()