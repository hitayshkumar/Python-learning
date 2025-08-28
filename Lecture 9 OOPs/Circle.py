class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2   # to the power 2
    def perimeter(self):
        return 2*3.14*self.r

r=float(input("Enter the radius of a circle in cm: "))
c1=Circle(r)
print("Area of the circle is : ",c1.area(),"sq cm")
print("Perimeter of the circle is :", c1.perimeter(),"cm")