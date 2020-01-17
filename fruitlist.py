# creating list of fruit storage
fruits = [1.5,2.3,3.5,1,2,2.25,2.75]
print( fruits)
sum=0
# iterating list
for item in fruits:
    sum+=item
else:
    bill=sum*50
    print("Bill is %0.2f rs for %0.3f kg of fruits" %(bill, sum))    

# indexing/ranging/slicing
print( fruits[3])
print(fruits[-2])
print(fruits[3:6])
print(fruits[-6:-2]) 
print(fruits[3: ])
print(fruits[ :20])

# adding new elements

fruits.append(2.5)
print(fruits)

# update an item

fruits[2]=1.75
print(fruits)

# delete an item

del fruits[4]
print(fruits)

# functions

print(len(fruits))
# returns largest and smallest item in list
print(max(fruits))
print(min(fruits))


ls=list("GITS#100")
print(ls)



