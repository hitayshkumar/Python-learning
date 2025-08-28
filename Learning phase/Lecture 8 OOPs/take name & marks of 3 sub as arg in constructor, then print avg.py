"""
class Stu:
    clg="ABC College"
    def __init__(self,name,phy,chem,math):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.math=math
    def avg(self):
        self.avrg=(self.phy+self.chem+self.math)/3
        print("The average marks of student are: ")
        return self.avrg

s1=Stu("karan",78,65,87)
print(s1.avg())
"""
#alternatively
class Stu:
    clg="ABC College"
    def __init__(self,name,marks):
        self.name=name    # obj attribute
        self.marks=marks   # obj attribute
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print(val)
        print("Hi,",self.name,"Your average marks are: ")
        self.avrg=sum/3
        return self.avrg

s1=Stu("karan",[78,65,87])
print(s1.avg())

s1.name="Hitesh"  # can also directly change object attribute
print(s1.avg())
s2=Stu("Nitin",[34,56,78])

print(s2.avg())
