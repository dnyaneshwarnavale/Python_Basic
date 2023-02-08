class Employee:
    no_if_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):  ## self nothing current object
        return  f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod   ## using this method change leave class lavel means rohan change leaves then these leaves are afftect to harry
    def change_leaves(cls,newleaves):
        cls.no_if_leaves=newleaves



harry=Employee("Harry",455,"Admin")
rohan=Employee("ROhan",555,"TL")

harry.change_leaves(20)

print(harry.no_if_leaves)

