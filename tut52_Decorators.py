def function1():
    print("subscribe now")

func2=function1  ## function copy is created and assign to func2
del function1
func2 ()

def funcreat(num):
    if(num==0):
        return  print
    if num==1:
        return  sum

a=funcreat(1)
print(a)

### decorator

def inner1(func):
    def inner2():
        print("Before function execution");
        func()
        print("After function execution")
    return inner2

@inner1
def function_to_be_used():
    print("This is inside the function")

function_to_be_used()