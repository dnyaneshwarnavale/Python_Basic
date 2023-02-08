###  Lambda function
minus =lambda x,y: x-y
print("Minus is:",minus(9,5))


## Lambda func using sort fun
def a_first(a):
    return a[1]

a=[[11,4],[7,6],[7,8]]
a.sort(key=lambda x:x[1])
print(a)