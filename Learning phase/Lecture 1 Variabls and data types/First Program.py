""" 
print ("hello world")
name = "Hitesh"
age = 32
price = 25.99

print("My name is",name)
print("I am",age,"years old")
print("Price =",price)

age2=age+10
print ("My age after 10 years is",age2)

print(type(name))
print(type(age))
print(type(price))


young= False
print(type(young))
print ( "I am young=",young)

a=None
print(type(a))
"""
# hi, I am a comment, Shortcut to comment = (Ctrl/)
#another method to comment multiple line is triple quotes (""")


# arihtmetic operators
"""
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #modulo operator
print(a**b) #power operator it means , a^b 
"""

# Relational Operators
"""
a=50
b=20

print(a==b) # will give False
print(a!=b) # Will give True
print(a>=b) #will give True
"""
#assignment operators
"""
num = 10
num += 10 # means num=num+10
print(num) # num becomes 20
num%=3 # means num= num%3
print(num) # num becomes 2
num**=5 # means num= num**5   , ** is power operator
print(num) # num becomes 32
"""

# Logical operators
"""
a=50
b=20
print(not(a>b))  # a>b is True but it will give false bc of not operator

val1 = True
val2= False
print("and operator:",val1 and val2)
print("not operator", val1 or val2)
print("or operator",(a!=b) and (a>b))
"""

# type conversion
"""
a= 2
b= 4.25
sum= a+b         #typeconversion done automatically on 'a' by interpreter, it converted int to float.
print("sum=",sum," Type=",type(sum))
"""

"""
a="2"
b=4.25
c=int(a) #typecasting, which is manual
sum=b+c
print(sum)
"""

"""
a= 3.14
a=str(a)
print(a, "type=",type(a))
"""

# taking input in python
"""
name = input("enter your name")
print("welcome,\nYou typed:",name)
"""

"""
age=int(input("Enter your age"))
print("Welcome,\nYou entered:",age)
name=input("Enter you name")
print("Hi,\nYou entered:", name,"\ntype of data is:",type(name))
"""