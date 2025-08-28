"""
marks={}
sub=input("Enter 1st subject name: ")
m=float(input("enter 1st subject marks: "))
marks[sub]=m

sub=input("Enter 2nd subject name: ")
m=float(input("enter 2nd subject marks: "))
marks[sub]=m
sub=input("Enter 3rd subject name: ")
m=float(input("enter 3rd subject marks: "))
marks[sub]=m
print(marks)
"""
# alternate method using update method

marks={}
x=int(input("Eneter phy: "))
marks.update({"phy": x})
x=int(input("Eneter chem: "))
marks.update({"chem": x})
x=int(input("Eneter Math: "))
marks.update({"Math": x})
print(marks)