class Employee:
    def __init__(self,role,deptt,sal):
        self.role=role
        self.deptt=deptt
        self.sal=sal
    def showdetails(self):
        print("Role: ",self.role,"\nDepartment: ",self.deptt,"\nSalary: ",self.sal)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",75000)


eng1=Engineer("Elon Musk",40)
eng1.showdetails()
