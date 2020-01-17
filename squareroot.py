import math
x=1
while x<=5:
    no = float(input("Enter no."))
    if no>=0:
        sq = math.sqrt(no)
        print("SQRT of %0.2f is %0.2f" %(no,sq))
        x+=1
    else:
        print("negative number")    
