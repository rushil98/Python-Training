import math
import re

class Basic:
    'to define basic operation'

    def areaCylinder(self,rad,hei):
        'to calculate area of cylinder'
        area=math.pi*rad*rad*hei
        print("Area is:%0.2f cm" %area)

    def countSymbol(self,str):
        'to count special symbols'
        # extracting all non alpha and non digits 
        symbols=re.findall('[^a-z0-9]',str,re.I)
        print("Size:%d" %len(symbols))
        for item in symbols:
            print(item,end="")
# inheriting base class
class Advanced(Basic):
    'to define new operations'

    def getNumbers(self):
        'to extract all numbers from str'
        str=input("Enter String:")
        numbers=re.findall('\d+[.]?\d*',str)
        print(numbers)

# creating an instance 
ad1=Advanced()
ad1.areaCylinder(20,40)
ad1.countSymbol("Gits@2020$4010 #12 ^Ram&")
ad1.getNumbers()