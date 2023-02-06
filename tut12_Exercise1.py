d1={
    "C": "C is programming Language",
    "C++":"C++ is Programming Language. It includes OOPs concept",
    "Angular":"Front End Programming Language",
    "SQL": "Its a database. provided by Microsoft"
}

print("All Dictionary Keys:", d1.keys())

print("Please ask to user enter the key")
str1=input()
print("Meaning of",str1,"is:",d1[str1])