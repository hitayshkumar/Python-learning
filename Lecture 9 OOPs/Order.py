class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,o2):  # dumder function used here, which means greater than
        return self.price>o2.price
           
o1=("chips",20)
o2=("tea",15)

print(o1>o2)  #true