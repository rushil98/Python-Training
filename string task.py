# string task

str=input("Enter Text:")
alpha,digits,spaces,symbols= 0,0,0,0
for ch in str:
    if ch.isalpha():
        alpha+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
    else: 
        symbols+=1
else:
    print("Alpha:%d\nDigits:%d\nSpaces:%d\nSymbols:%d"%(alpha,digits,spaces,symbols))
    size = len(str)
    print("size:%d"%size)
    if symbols>=size*0.2:
        print("String is not meaningful")
    else:
        print("Meaningful string")                 