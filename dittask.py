# creating dict to store account details

ACINFO = {}
def add_act_info():
    'to add new account info'
    an=int(input("Enter account number:"))
    ahn=input("Enter Ac name:")
    ab=float(input("Enter accout balance:"))
    pin=int(input("Enter Account PIN:"))
    ACINFO[an]=[ahn,ab,pin]

    # adding into dict

def read_act_info():
    'to read all account info'

    for info in ACINFO:
        print("%d\t%s\t%0.2f\t%d"\
            %(info,ACINFO[info][0],ACINFO[info][1],ACINFO[info][2]))

def withdraw(an,amt):
    "to withdraw from account"

    if an in ACINFO:
        pn=int(input("Enter PIN:"))
        if ACINFO[an][1]>=amt and ACINFO[an][2]==pn:
            ACINFO[an][1]-=amt
            print("Cur balance:%0.2f Rs"%ACINFO[an][1])
        else:
            print("Given Ac no is not valid")

def deposit(an,amt):
    "to deposit into account"
    if an in ACINFO:
        ACINFO [an][1]+=amt
        print("Cur Bal: %0.2f Rs" %ACINFO[an][1]) 
    else:
        print("Given acin not valid") 

# calling function

for i in range(2):
    add_act_info()
else:
    read_act_info()
withdraw(5502,3000)
deposit(5503,2000)                              
