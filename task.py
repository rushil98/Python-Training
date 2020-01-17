import random
i=1

while i<=1000:
    no = random.randint(48,123)
    print(chr(no),end="")
    if no in range(65,91):
        count1+=1
        print("Lowercase characters are",count1)
    elif no in range(97,123):
        count2+=1
    elif no in range(48,58)
    count3+=1
            