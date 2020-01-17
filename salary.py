basic=int(input("Enter salary:"))
if basic>=10000:
    ta=(10/100)*basic
    da=(15/100)*basic
    hra=(20/100)*basic
else:
    ta=(15/100)*basic
    da=(20/100)*basic
    hra=(30/100)*basic
total=(ta+da+hra+basic)    
print("gross:",total)
    

