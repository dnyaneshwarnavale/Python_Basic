a=9
b=9
c=sum((a,b))
print(c)

#user defined function

def func1():
    print("Hello  u r in function")
func1()

## func value
def func2(a,b):
    print("Addition is:",a+b)
func2(10,20)

## func return value
def func3(a,b):
   average=(a+b)/2
   return average

v=func3(10,20)
print("Average value is:",v)

## docstring :
def func4(a,b):
   """" This is afunc to calculate avg of 2 numbers"""
   average=(a+b)/2
   return average

print(func4.__doc__)
v=func4(10,20)
print("Average value is:",v)

