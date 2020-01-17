FR=None
try:
    FILENAME= input("Enter file Name:")
    # opening file in read mode
    FR=open(FILENAME)
    lines=FR.readlines()
    Balance=float(lines[2])
    no = int(input("Enter no of people:"))
    Rs = Balance/no
    print("Per person Rs: %0.2f"%Rs)
    print("Welldone")
    #FR.close()
except Exception as ex:
    print(type(ex),":",ex)
finally:
    if FR:
        FR.close()
        print("File Closed")
print("All is Well")            



