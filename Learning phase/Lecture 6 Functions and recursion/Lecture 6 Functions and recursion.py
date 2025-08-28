# functions
# a function to add two numbers and return the sum
"""
def sum(a,b):
    s=a+b
    return s

a=int(input("1st number"))
b=int(input("2nd number"))
print(sum(a,b)) #function call inside print()
"""
# alternatively
"""
def sum(a,b):
    sum=a+b
    print(sum) #printing directly and returning nothing
    return sum # in case we called a fucntion and expected a return we would get "None"

a=int(input("1st number"))
b=int(input("2nd number"))
sum(a,b)    #fcuntion call
"""

# alternatively
"""
def sum(a,b):
    sum=a+b
    print(sum) #printing directly and returning nothing
    return sum # in case we called a fucntion and expected a return we would get error hence we returned for safety


sum(input("1st nunber"),input("2nd number")) #function call

"""

# default parameters
"""
def calc (a=1,b=1):
    return a*b

print(calc())

"""
 

