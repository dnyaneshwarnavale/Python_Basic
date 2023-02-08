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
        # params=string.split("*")
        # print(params)
        # return cls (params[0],params[1],params[2])
        return cls(*string.split("*"))



harry=Employee("Harry",455,"Admin")
rohan=Employee("ROhan",555,"TL")
karan=Employee.from_str("Karan*180*student")

print(karan.printdetails())
rohan.change_leaves(50)
print(harry.no_if_leaves)

