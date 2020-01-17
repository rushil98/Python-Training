class Card:

    'to represent card info and operations'

Card=input("Enter something for Card:")

def __int__(self):
    'to initialize card info'
    self.CNo=int(input("Enter Card No.:"))
    self.CHName=input("Enter Card holder name: ")
    self.CBalance=float(input("Enter Card Balance:"))
    self.CExdate=input("Enter Expiry Date:")

def getCardInfo(self):
    'to display card info'
    print("Card No: %d" %self.CNo)
    print("Card Name: %s" %self.CHName)
    print("Card Balance: %0.2f" %self.CBalance)
    print("Card Expiry Date: %s" %self.CExdate)

def withdraw(self,amt):
    'to withdraw from account balance'
    if self.CBalance>=amt:
        self.CBalance-=amt
        print("Your Card Balance(Withdraw):%0.2f Rs" %self.CBalance) 
    else:
        print("Low Balance")

def deposit(self,amt):
    'to deposit into balance' 
    self.CBalance+=amt
    print("Current card balance(Deposit):%0.2f Rs"%self.CBalance)

# inheriting into Derived Class
class DebitCard(Card):
    'to describe/represent Debit Card info and operations'

    Msg=input("Enter Message:")

    def __init__(self,pin):
        'to initialize Debit Info'
        # calling base class __init__
        Card.__init__(self)
        self.PIN=pin

    def getDebitInfo(self):
        'to display Debit Info'
        self.getCardInfo()
        print("PIN: %d" %self.PIN)

    def withdraw(self,amt):
        'to withdraw from account balance'
        pin=int(inout("Enter PIN:"))
        if self.CBalance>=amt and self.PIN==pin:
            self.CBalance-=amt
            print("Debit Balance (Withdraw):%0.2f Rs" %self.CBalance)
        else:
            print("Low Balance or Wrong PIN")     

# functions
print(issubclass(DebitCard,Card))               

# creating instance
dc1=DebitCard(2345)
print(isinstance(dc1,DebitCard))
dc1.getDebitInfo()
dc1.withdraw(10000)
dc1.deposit(20000)                               
