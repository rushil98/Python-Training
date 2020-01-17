# creating dict to account detail

ACINFO={}
for i in range(2):
    an=int(input("Enter account number:"))
    ahn=str(input("Enter account Holder name:"))
    ab=float(input("Enter account balance:"))
    pin=int(input("Enter PIN:"))

    # adding info in dict
    ACINFO[an]=[ahn,ab,pin]
else:
    print(ACINFO)

#withdraw     
