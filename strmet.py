# string methods
info = "India $100 UDR @19"
#returns size of given str
print(len(info))
# returns an index of given str
print(info.index("$100"))
# returns no of occurances
print(info.count("0"))
# checking all chars for alpha or num
print(info.isalnum())
# checking all chars are alpha
print(info.isalpha())
# checking all chars are num
print("5050".isdigit())
# checking all chars are spaces
print("    ".isspace())
# replacing spaces with"-"
print(info.replace(" ","-"))
# checking all chars are in lower case
print(info.islower())
# checking all chars are in upper case
print(info.isupper())
print(info.capitalize())
# swapping case
print(info.swapcase())
# returns list of tokens splitted byb given str
tokens=info.split("1")
print(tokens)