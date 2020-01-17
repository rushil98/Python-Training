info="GITS@2019"
for ch in info:
    if ch not in"aeiouAEIOU":
        print(ch,end="")

    c=0
    for ch in info:
        if ch in "0123456789":
            c+=1
print(c)
