class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}.{lname}@email.com"
    def explain(self):
        return f"This is employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set"
        return f"The email address is {self.fname}.{self.lname}@email.com"

    @email.setter
    def email(self,string):
        print("Value setter")
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

ram=Employee("Ram","Mane")
shyam=Employee("Shyam","Shinde")

ram.fname="Raman"
print(ram.explain())

ram.email="this.that@email.com"
print(ram.email)

del ram.email
print(ram.email)