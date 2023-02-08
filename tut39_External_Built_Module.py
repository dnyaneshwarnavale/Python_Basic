import random
import calendar
random_number=random.randint(0,5)
print(random_number)

rand=random.random() *10
print(rand)

lst=["C lan","C++","C#","Java"]
print("choice function:",random.choice(lst))

yer=int(input("Enter year:"))
cal=calendar.isleap(yer)
if (cal== True):
    print("Leep year")
else:
    print("Not leep year")


