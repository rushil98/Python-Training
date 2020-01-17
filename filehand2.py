FILE_NAME = "acinfo.txt"

def add_act_info():
    "to add new account info into file"
    an =input("Enter AC no.:")
    ab = input("Enter AC balance:")
    pin = input("Enter account PIN:")
    ahn = input("Enter Account holder's name:")
    # opening file in append mode
    writer=open(FILE_NAME,"a")
    writer.write(an+"\t"+ab+"\t"+pin+"\t"+ahn+"\n")
    writer.close()
    print("Values have been added to the file")

def read_act_info():
    "Read values from the file"
    reader=open(FILE_NAME)
    # reading all lines and returns list of lines
    lines = reader.readlines()
    for line in lines:
        print(line,end="")
    else:
        reader.close()
# calling function
for i in range(2):
    add_act_info()
read_act_info()           