# to print 5,4,3,2,1
"""
def show (n):
    if(n==0):
        print('n=',n,sep='')
        return # return returns down layer by layer from the call stack and runs the function until all layers are deleted
    print(n)
    show(n-1)
    print("end") # will print 'n' times after exeuting return beause of call stack concept

show(5)

"""

# to print factorial of n using recursion
# logic of recurrence fact(n)= fact(n-1)*n

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

n=int(input("Enter the number to find factorial of using recursion:"))
print(fact(n))