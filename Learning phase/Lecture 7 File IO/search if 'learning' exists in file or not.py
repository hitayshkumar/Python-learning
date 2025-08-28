
def srch(s):
    with open("practice.txt","r") as f:
        data = f.read()
        idx=data.find(s) #find method in string used here
        if idx!=-1:
            print("Found at index : ",idx)
        else:
            print("not found")
    f.close()

strng=input(" Enter the keyword you need to search for:")
srch(strng)