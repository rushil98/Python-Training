pm=int(input ("Pocket money:"))
em=pm/2
print("We can spend %0.2f rs" %em)
if em>=1000:
    print("Shopping")
    print("We have ",em,"rs")
else:
    print("Movies") 
    print("balance ",em,"rs")   
print("Thank You")
