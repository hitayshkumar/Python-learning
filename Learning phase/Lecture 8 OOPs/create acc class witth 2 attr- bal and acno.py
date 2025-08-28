class Account:
    def __init__(self,bal,acno):
        self.balance=bal
        self.acno=acno
    def debit(self,amt):
        self.balance-=amt
        print("Rs",amt," debited")
        print(" Balance=",self.bal())

    def credit(self,amt):
        self.balance+=amt
        print("Rs",amt," credited")
        print(" Balance=",self.bal())

    def bal(self):
        return self.balance



ac1=Account(10000,12345678)
ac1.debit(1000)
ac1.credit(500)
ac1.bal()
