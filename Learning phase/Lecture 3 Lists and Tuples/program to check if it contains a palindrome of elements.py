a=[1,2,3,2,1]
b=a.copy()
b.reverse()
if(b==a):
    print("yes, the list contains a palindrome of elements")
else:
    print("no, the list doesn't contain a palindrome of elements")
print(a,b)