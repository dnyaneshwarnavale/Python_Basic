"""
Iterable
Iterator
Iteration
"""

def gen(n):
    for i in range(n):
        yield i

r=gen(3)
print(r.__next__())
print(r.__next__())
print(r.__next__())
#print(r.__next__())  # its give an error message

h="harry"
ier=iter(h)
print(ier.__next__())
print(ier.__next__())

# for c in h:
#     print(c)


