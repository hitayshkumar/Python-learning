#while loop
"""
n=1
while n<=5:
    print("hello") 
    n+=1

# while loop with multiple conditions
n=1
while n<5 or n==5:
    print("hello2")
    n+=1

"""
"""
n=1
while n<=100000:
    print(n,") College")
    n+=1


"""

#using break:
"""
i=1
while i<=5:
    print(i)
    if( i==3 ):
        break
    i+=1
print("end of loop")

"""

# using break in the number search program
"""
nums=(1,4,9,16,25,36,49,64,81,100,36)
i=0
n=int(input("enter the number you want to seaerch: "))
while i<len(nums):
    if(n==nums[i]):
        print("Found at:",i)
        break
    i+=1
    
"""

#using continue
"""
i=1
while i<=5:
    if(i==3): #skips printing 3 but also skips counting
        i+=1   #therefore we need to count here as well
        continue
    else:
        print(i)
    i+=1

"""

#for loop
# specially used while traversing in a data type which is linear in nature eg. tuple, list, string etc.
"""
nums=[1,2,3,4,5]
for val in nums:
    print(val)

"""
"""
veg=["potato","brinjal","tomatoes","onion"]
for val in veg:
    print(val)

"""

"""
tup= (1,2,3,4,5,6,7,8,9)
for num in tup:
    print(num)
"""

"""
str="college"
for ch in str:
    print(ch)
"""

#for loop whith else

""""
str="apnaCollege"
for ch in str:
    if(ch=="o"): #searching for o
        print("o found")
        break
    print(ch)
else:
    print("full string searched")
"""

# range() # range function

"""
seq=range(5)
for i in seq:
    print(seq[i])
"""

# code to print numbers from 1 to 10 using range() and for loop
"""
for i in range(10):
    print(i+1)
"""

# code to print numbers from 10 to 1000 with diff of 10 steps
"""
for i in range(10,1000,10): #range(start?, stop, stepsize?)
    print(i)
"""
#multiplication table using for loop and range()
"""
n=int(input("Enter the number to find multiplication table for: "))
for i in range(1,11,1):
    print(n,"x",i,"=",i*n)

"""

#print numbers from 100 to 1 using for loop and range()
"""
for i in range (101):
    if (100-i==0):
        break
    print(100-i)
"""
# alternate method
"""
for i in range(100,0,-1): # -1 is used as negative step
    print(i)
"""

# pass statement - placeholder for future code, 
"""
for i in range(5):
    pass
if i>5:
    pass
print("passed")

"""