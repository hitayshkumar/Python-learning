t=(1,4,9,16,25,36,49,64,81,100)
n=int(input("enter the number to search: "))
a=0
for val in t:
    if(n==val):
        print("Found at index: ",a)
        break
    a+=1
else:
    print("not found")
