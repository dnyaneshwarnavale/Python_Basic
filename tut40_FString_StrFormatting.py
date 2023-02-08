# F string
##  string format
import math

me="Harry"
a1=3
a ="This is %s %s"%(me,a1)
print(a)

####  another example
a11= "This is {1} {0}"
b= a11.format(me,a1)
print(b)

## 3rd way
aa=f"this is {me} {a1} {math.cos(65)}"
print(aa)
