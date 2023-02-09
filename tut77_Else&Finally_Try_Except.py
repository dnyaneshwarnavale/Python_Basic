f1=open("SampleFile.txt")

try:
    f=open("does.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running.... ")
finally:
    print("in finally block")
    f1.close()
    #f.close()

print("out of try block")