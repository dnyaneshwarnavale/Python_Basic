# public
# protected
# private

class Employee:
    no_if_leaves=8
    var=90
    _protect=9
    __pr=90
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

emp=Employee("harry",333,"Programmer")
print(emp._Employee__pr)
