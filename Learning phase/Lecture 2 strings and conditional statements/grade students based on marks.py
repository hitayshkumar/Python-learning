marks= int(input("Enter absolute marks of the student: "))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade ="C"
elif(marks>=60 and marks<70):
    grade ="D"
else:
    grade ="F"
print("Grade of the student is:",grade)