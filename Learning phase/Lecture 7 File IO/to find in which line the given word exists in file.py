
def srch(s):
    with open("practice.txt","r") as f:
        data = f.read()
        idx=data.find(s) #find method in string used here
        if idx!=-1:
            print("Found at index : ",idx)
        else:
            print("not found")
    f.close()

def chkln(s):
    with open("practice.txt","r") as f:
        data= True
        lno=1
        while data:
            dat=f.readline()
            if s in dat: # better syntax than data.find(s)
                print("Found in line number:",lno)
                return
            lno+=1
    f.close()

strng=input(" Enter the keyword you need to search for:")
srch(strng)
chkln(strng)
