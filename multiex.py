import datetime


def getGross(basic):
    'to calc gross salary'
    gross=basic+basic*0.1+basic*0.3
    print("Salary is :%0.2f Rs" %gross)

try:
    city={11:'New Delhi',22:'Mumbai',44:'Chennai',294:'Udaipur'}
    std=int(input("Enter STD Code:"))
    print("%d is code of %s"%(std,city[std]))
    # calling fun
    getGross(6000)
    getGross("7500")
    fr=open(input("Enter File Name:"))
    print(fr.read())
    fr.close()
    print("Everything is fine")
except ValueError as ve:
    print("Enter correct value :%s"%ve)
except KeyError as ke:
    print("Given code %d is not in STD List:%s" %(std,ke))
except Exception as ex:
    fw=open("errlog.txt","a")
    # returns current time and date
    cdt=datetime.datetime.now()
    fw.write(str(cdt)+"\t\t"+str(type(ex))+"\t"+str(ex)+"\n") 
    fw.close()
    print("Error Logged")
print("All is Well")
  
