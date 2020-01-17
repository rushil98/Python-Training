import random
for i in range(20):
    ch=input("Input character between A to Z")
    no=random.randint(65,90)
    gen_ch = chr(no)
    if ch == gen_ch:
        print("Winner")
        break
else:
    print("Try Again")

