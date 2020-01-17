# creating/opening file in writing mode

fw=open ("emp47.txt","w")
# writing data into file
fw.write("341001\n")
fw.write("Rushil Agarwal\n")
fw.write(input("Enter mobile no:") )
fw.write("\n")
fw.write(input("Enter Address:"))
fw.close()
print("Data written in file")
# opening file in reading mode

fr=open("emp47.txt")
# reading from file
data=fr.read()
# closing file
fr.close()
print("File Data :\n%s" %data)