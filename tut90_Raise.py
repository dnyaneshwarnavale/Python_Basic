a= input("what is u r name")
b=input("How much di you earn")

if int(b)==0:
    raise ZeroDivisionError("b is 0")

if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello {a}")

