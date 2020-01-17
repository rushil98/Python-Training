# creating list
score=[90,56,44,32,45,90,44] 
# adding new item 
score.append(82)
print(score)
# returns no of occurances
print(score.count(90))
extra=[22,56]
#extending list
score.extend(extra)
print(score)
# returns an index of given item
print(score.index(45))
# inserting at specified index
score.insert(3,51)
print(score)
# removes last item if index is not there
score.pop(2)
print(score)
# remove given item
score.remove(44)
print(score)
# reversing list
score.reverse()
print(score)

# sort in ascending order
score.sort()
print(score)

# in descending order
score.sort(reverse=True)
print(score)

