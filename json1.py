import json
emp_file="empinfo.json"

def read_emp_info():
    "To read data from json"
    # opening json file
    fr=open(emp_file)
    # reading all data into python compatible form
    info=json.load(fr)
    fr.close()
    for item in info:
        print("%d\t%s\t%0.2f"%(item["ecode"],item["ename"],item["esal"]))

def add_emp_info():
    "to add new emp detail"
    fr=open(emp_file)
    info=json.load(fr)
    fr.close()
    ec=int(input("Enter emp code:")) 
    en=input("Enter emp name:")
    es=float(input("Enter emp salary:"))
    # creating dict
    data={'ecode':ec,'ename':en,'esal':es}
    # appending into list
    info.append(data)
    # opening file in write mode
    fw=open(emp_file,"w")
    # dumping list into file
    json.dump(info,fw)
    fw.close()
    print("Emp info saved") 


# calling functions
read_emp_info()
add_emp_info()
read_emp_info()      