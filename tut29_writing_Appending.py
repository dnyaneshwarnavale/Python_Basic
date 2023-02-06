f=open("FileWriting.txt","a")
a=f.write("This is thrid line\n")
print("Number of char emntered in file",a)

f.close()

# handle read & write both
f=open("FileWriting.txt","r+")
print("Reading data from file:\n",f.read())

f.close()