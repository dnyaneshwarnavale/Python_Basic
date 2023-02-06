mystr="Athesh is a good boy"
print(mystr)
print(len(mystr))

print(mystr[4])
print(mystr[0:4]) ## 4 is exclude means char from 0 to 3
print(mystr[0:5:2]) ## skip char - means 2 is print 0 3 5 position char
print(mystr[::]) ## default last is 1 so its print all char  --  advanced slicing

##negitive index
print(mystr[-1:-4]) # -1 is last char

# string function
print(type(mystr))
print(mystr.isalnum()) # false becoz spaces
print(mystr.endswith("bdoy"))
print(mystr.count('o')) # count passed char
print(mystr.find("is"))


