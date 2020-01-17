# creating tuples to store marks
marks=(95,86,64,52,44,95)
print(marks)
# iterating tuple
for item in marks:
    print(item)
#indexing/slicing/ranging
print(marks[3])
print(marks[-5])
print(marks[2:6])
print(marks[-6:-3])
print(marks[-4])
print(marks[ :-2])    
# functions on tuple
print(len(marks))
print(max(marks))
print(min(marks))
tp=tuple("INDIA$12")
print(tp)

# methods

print(marks.count(95))
print(marks.index(44))

