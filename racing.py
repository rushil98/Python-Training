rd=int(input("Enter racing distance:"))
if rd>=3000:
    rate=25
    print("platinum")
elif rd>=2000:
    rate=20
    print("gold")
elif rd>=1000:
    rate=15
    print("silver")
else:
    rate=10
    print("bronze")
cash=rd*rate    
print("Prize is:%0.2f rs"%cash)

