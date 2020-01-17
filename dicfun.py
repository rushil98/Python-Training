# creating dict to store book details

books={"PE1201":450.90,"PE1204":670.50,"PE1202":1040.90}
# returns a copy of dict
info=books.copy()
print(info)
print(books.fromkeys("INDIA$50",25))
ecode=[22001,22005,22009,22010]
# returns dict by extracting given sequence with default values
print(books.fromkeys(ecode,1100))
# returns value of given key
print(books.get("PE1204"))
# returns list of tuples(key,value)
print(books.items())
# returns list of keys
print(books.keys())
# returns list of values
print(books.values())
# add new items if key is not available
books.setdefault("PE1205",1150.50)
print(books)
# merging into books dict
books.update({ "PE1206":850.60,"PE1207":250.30})
print(books)
#clearing data of dictionary but keeping the dictionary 
books.clear()
