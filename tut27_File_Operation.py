# File IO Basics
"""
"r" - open file for reading - default
w - open file for writing
x - create files if not exists
a - add more content append
t - text mode - default
b - binary mode
+ - read and write

 """

## file writing
f=open("SampleFile.txt")
content=f.read()
print(content)

f.close()
## read mode
f=open("SampleFile.txt","r")
content=f.read()  # content=f.read(3)
print(content)

f.close()

# line by line read
f=open("SampleFile.txt","rt")
content=f.read()
for line in f:
    print(line, end="")
f.close()

# line by line read
f=open("SampleFile.txt","rt")
print(f.readline())

f.close()



