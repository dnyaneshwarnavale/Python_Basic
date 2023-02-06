grocery=["Harpic","Vim bar","Bhindi","Lollypop"]
print(grocery)
print(grocery[2])

numbers=[2,7,9,11,3]
print(numbers[2])
numbers.sort()
numbers.reverse()
print(numbers)

##slicing
print(numbers[0:5])
print(numbers[:5])
print(numbers[:])

numbers.append(7)
numbers.insert(1,67)
print(numbers)

# tuples   -- value not changed
#nutable - can change
#Immutable - can not change
#tp=(1,) # if in tuple one value the need to add , in ast value
tp =(1,2,3)
tp[1]=8
print(tp)
