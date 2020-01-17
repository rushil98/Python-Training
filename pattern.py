# pattern printing
row=int(input("Enter rows:"))
for r in range (1, row+1):
    c=1
    sum=0
    while c<=r:
        print(c,end='\t')
        sum+=c
        c+=1
    else:
        print(sum,end='\t')
        sum=0
        print()
else:
    print("DONE")            
