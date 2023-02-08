class Employee:
    no_if_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):  ## self nothing current object
        return  f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_if_leaves=newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("*"))

    @staticmethod
    def printGood(string):
        print("This is good" + string)
        #return "ACB"

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,language):
        self.name = aname   ## here we can super keyword for accessing base class 
        self.salary = asalary
        self.role = arole
        self.language=language
    def printprog(self):
        return f"The programmer Name is {self.name}, Salary is {self.salary} and role is {self.role}. The languages are{self.language}"



harry=Employee("Harry",455,"Admin")
rohan=Employee("ROhan",555,"TL")

shubham=Programmer("shubham",777,"Programmer",["python","C"])
karan=Programmer("KAran",999,"Prog",["C++","python","DotNet"])
print(karan.printprog())

