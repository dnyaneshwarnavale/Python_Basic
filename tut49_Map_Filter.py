numbers=["3","34","56","78"]

for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

numbers[2]=numbers[2]+1
print(numbers[2])

## using MAP
numbers=["3","34","56","78"]

numbers=list(map(int,numbers))
numbers[2]=numbers[2]+1
print("Using Map:",numbers[2])

num=[2,3,4,5,6]
square=list(map(lambda x: x*x,num))
print(square)