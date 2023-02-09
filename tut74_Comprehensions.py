ls=[]
for i in range(100):
    if(i%3==0):
        ls.append(i)

print(ls)

## using list comprehensions -- using []

ls2=[i for i in range(100) if i%3==0]
print (ls2)

##using dictionary comprehensions -- using {}
dict1={ i:f"item{i}" for i in range(5) ## start from 1 instead of 0
        }
dict2={value:key for key,value in dict1.items()}

print(dict1)
print(dict2)

## using SET comprehensions  ## return single set -- using {}
dresses={dress for dress in ["dress1","dress2","dress3","dress4","dress5","dress1","dress1"]}
print(dresses)

## using Generator comprehension -- using ()
evens =(i for i in range(100) if i%2==0)
print(evens)
print(evens.__next__())
