def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f
n=int(input("Enter the number to find its factorial: "))
print(fact(n))
