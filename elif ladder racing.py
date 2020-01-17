rd=(int(input("Enter racing distance:"))
if rd>=3000:
    rate=25
    print("platinum")
elif rd>=2000:
    rate=20
    print("gold")
elif rd>=1000:
    rate=15
    print("silver")
else rd>=500:
    rate=10
    print("bronze")
print("Prize is: "rate)

