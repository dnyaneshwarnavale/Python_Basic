
no=10 #Global variable
def func1(n):
    no=5  # local variable
    print(no)
    print("N values",n)

func1("This is me")
print(no)

## Global keyword
no=10 #Global variable
def func1(n):
    global no  # local variable
    no=no+10
    print(no)
    print("N values",n)

func1("This is me")
print(no)

#nested function with global keyword
def harry():
    x=100
    def rohan():
        global x
        x=80
    print("Before calling rohan",x)
    rohan()
    print("After calling rohan",x)

harry()