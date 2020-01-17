# break example

import random

while True:
    # returns no between 0.0 and 1.0
    no = int(random.random()*100)
    print(no)
    if no>=9:
        # terminating loop
        break
else:
    print("Completed")

str=input("Enter text")
for ch in str:
    # converting into ascii
    code=ord(ch)
    if code in range(48,58) or code in range(65,91) or code in range(97,123) or ch==" ":
        print(ch,end="")
    else:
        break
else:
    print("Completed")
print()

for ch in str:
    # converting into ascii
    code = ord(ch)
    if code in range(48,58) or code in range(65,91) or code in range(97,123):
        print(ch,end="")
    else:
        continue
else:
    print("Done")    

i=0
while i<=1000:
    i+=1
    if i%7 !=0:
        # goes to condition
        continue
    print(i)
else:
    print("Done")


class Account:
    pass
if 40 in range(40,45)
    pass

