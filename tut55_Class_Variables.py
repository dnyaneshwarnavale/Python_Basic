class Employee:
    no_if_leaves=8
    pass

harry=Employee()
rohan=Employee()

harry.name ="Harry"
harry.salary=1234
harry.role="Admin"

rohan.name="Rohan"
rohan.salary=3434
rohan.role="TL"

print(harry.name)
print(Employee.no_if_leaves)

Employee.no_if_leaves=9
print(Employee.no_if_leaves)

print(Employee.__dict__)
print(rohan.__dict__)
print(harry.__dict__)