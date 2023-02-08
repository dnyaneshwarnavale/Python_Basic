class A:
    classaVar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classaVar1="Instance var of class A"
        self.special="special"

class B(A):
    classaVar1 = "I am a class variable in class B"

    def __init__(self):
        #    super().__init__()
        self.var2 = "I am inside class B's constructor"
        self.classaVar1 = "Instance var of class B"
        super().__init__()

a= A()
b= B()

print(b.special,b.var1,b.classaVar1)
