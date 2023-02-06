var1="hello world"
var2=4
var3=36.7

print(var3)
print((type(var1)))
print((type(var2)))
print((type(var3)))

var4="50"
var5="60"
print(int(var4)+ int(var5)) # need to typecast into partucluar language
print(5* "Hello world\n") ## 5 times multiple times

# Declare a variable and initialize it
f = 101
print (f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print (f)
someFunction()
print (f)


# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)


## take input from user
print("Enter first Number:")
num1= input()

print("Enter second Number:")
num2= input()

print("Addition is: ", int(num1)+int(num2))