print("enter num1 value:")
num1=input()
print("enter num2 value:")
num2=input()

try:
 print("Addition of 2 number:", int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is next line")
