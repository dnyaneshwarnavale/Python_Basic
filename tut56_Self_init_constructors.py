class Employee:
    no_if_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):  ## self nothing current object
        return  f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

harry=Employee("Harry",455,"Admin")
#rohan=Employee()
print(harry.salary)

# harry.name ="Harry"
# harry.salary=1234
# harry.role="Admin"
#
# rohan.name="Rohan"
# rohan.salary=3434
# rohan.role="TL"

