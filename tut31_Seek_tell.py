f=open("FileWriting.txt")
#print(f.tell())
print(f.readline())
#print(f.tell())
f.seek(10) # file pointer at particular position
print(f.readline())
#print(f.tell())
print(f.readline())


