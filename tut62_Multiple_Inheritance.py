from builtins import print


class Employee:
    no_if_leaves=8
    var=8
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

class Player:
    no_of_games=4
    var=9
    def __init__(self,name,games):
        self.name=name
        self.game=games

    def printdetails(self):
        return f"Name is {self.name}, Game is {self.game}"

class CoolProgrammer(Employee,Player):
    language="C++"
    var=10
    def printLanguage(self):
        print(self.language)


harry = Employee("Harry", 455, "Admin")
rohan = Employee("ROhan", 555, "TL")

shubham=Player("Shubham",["cricket","football"])
karan=CoolProgrammer("karan",899,"CoolProgrammer")
det=karan.printdetails()
# karan.printLanguage()
print(det)
print(karan.var)
