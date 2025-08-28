# creating class
"""
class Student: # creating class
    name = 'karan kumar'
s1= Student()  # creating obj of calss student
print(s1.name)

"""
"""
class Car:
    color = 'blue'
    brand = 'mercedes'
c1= Car()
print(c1.color)
print(c1.brand)

"""

#__init__()
"""
class Student: # creating class
    def __init__(self, fullname): # self or any abcd named variable is always an argument in def fn, #fullname is arg input when obj is created
        self.name=fullname # name is a variable created in class student
        print("creating new student")
    name = 'karan kumar'

s1= Student("hitesh")
"""
#also valid
"""
class Student: # creating class
    def __init__(abc, fullname): # self or any abcd named variable is always an argument in def fn, #fullname is arg input when obj is created
        abc.name=fullname # name is a variable created in class student
        print("creating new student")
    name = 'karan kumar'

s1= Student("hitesh")
"""

# create a class for students and save their data in a file
"""
class Stu:
    def __init__(self,nm,mk):
        self.name=nm
        self.marks=mk
    print("data added in class successfully")

s1= Stu("Hitesh",72)
s2= Stu("Nitin",87)
s3= Stu("Rohit",98)

print(s1.name,s1.marks,s2.name,s2.marks,s3.name,s3.marks,end=" ")

with open("student data.txt","a") as f: # writing data to a file
    f.write(s1.name)
    f.write(str(s1.marks))
    f.write(s2.name)
    f.write(str(s2.marks))
    f.write(s3.name)
    f.write(str(s3.marks))
print("data added to file successfully")
"""

# two categories of constructors
"""
class Stu:
    def __init__(self): # default constructor, not necessary to type
        print("adding new data")
        m="test dafault"
    def __init__(self,nm,mk): # parameterized constructor - takes custom parameter 
        self.name=nm
        self.marks=mk
    print("data added in class successfully")

s2=Stu("hitesh",87)
print(s2.name,s2.marks)
"""

# attributes
"""
class Stu:
    clg_name="ABC college"   # class attribute
    name='anonymous'
    def __init__(self,nm,mk):
        self.name=nm    # obj/instance attribute
        self.marks=mk
    print("data added in class successfully")

s1= Stu("Hitesh",72)
s2= Stu("Nitin",87)
s3= Stu("Rohit",98)
print(s1.clg_name,s1.name,s1.marks,"\n",s2.clg_name,s2.name,s2.marks)
# also valid
print(Stu.clg_name)
print(s1.name)  #call for obj attribute obj.attr > cls.attr
"""

#methods
"""
class Stu:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def hello(self): # fn that belong to obj
        print("hello",self.name)
    def mrk (self):
        return self.marks
s1= Stu("karan",97)
s1.hello()
print(s1.mrk())
"""

#static methods  - that don't use self parameter  ( we use decorator for that purpose)

"""
class Stu:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def hello(self): # fn that belong to obj
        print("hello",self.name)
    @staticmethod #decorator - converts normal mehtod to static method
    def sthello():  # doesn't use self parameter
        print("static method")

        
    def mrk (self):
        return self.marks
    
s1= Stu("karan",97)
s1.hello()
s1.sthello()
print(s1.mrk())
"""
