def func_name_print(a,b,c,d):
    print(a,b,c,d)

func_name_print("aa","bb","cc","dd")

## *args - arguments
def funcargs(*args):
    for item in args:
     print(item)

uname=["aa","bb","cc","dd"]
funcargs(*uname)

##kwargs  - arguments mainly used in dictionary

def funckwargs(**kwargs):
    for key, value in kwargs.items():
     print(key,value)

uname1={"Rohan":"C++ prog","Ram":"Net prog","Shaym":"cloud"}
funckwargs(**uname1)