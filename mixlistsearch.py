# creating list to store mixed values:

mix=[12001,"parth ameta",12300.90,4j+3,"GITS@2019",[120,"Android"],(30,"flex",450.90),450,234.5590]

#iterating list
for item in mix:
    if type(item) in [int,float,complex]:
        print( item )

# creating list to store names

names=[]
for i in range(5):
    n = input("Enter student name:")
    #adding into list
    names.append(n)
else:
    print(names)
# searching name
search=input("Enter name to search:")
for item in names:
    if search in item:
        print(item)        