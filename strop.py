# string operators
str= "Gits, RAj@2020"

#concatination
print(str+ "India")

# repeatation
print("India"*5)

#indexing/ranging/slicing
print(ste[11])
print(ste[-4])
print(ste[4:11])    # from 4 to 10
print(ste[-11:-2])  # from -11 to -3
print(ste[-4:-10])  #  nothing
print(ste[3:])  # from 3 to end
print([ :7])    #from 0 to 6
print([-3: 15])     #from 11 to 14

if "city" in "udaipur city":
    print("City Name")

# raw string
 
AcNO=121001
Acname="Rushil"
Acbal=14500.0
str=r"Hello %s, \nU have bal\t%0.2f\trs in ac no\t\t%d,\ngood\b\brs"\
    %(Acname,Acbal,AcNO)
print(str)
str="Hello{1},Bal is{0}in Acno{2},well done".format{Acbal,Acname,AcNO}
print{str}        