########   iterative method
def factorial_iterative(n):
    """
     return n*n-1 * n-2 * n-3
    """
    fac=1
    for i in range(n):
        fac=fac * (i+1)
    return fac

########  Recursive  method
def factorial_Recursive(n):
    """
     return n*n-1 * n-2 * n-3
    """
    if n==1:
        return 1
    else:
        return n * factorial_Recursive(n-1)


### Fibonacci series
def fibonacci(n):
    if n==0:
        return  0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num=int(input("Enter the number for calculate factorial:\n"))
print("Factorial Number using Iterative : ", factorial_iterative(num))
print("Factorial Number using Recursive : ", factorial_Recursive(num))
print("Fibonacci series:",fibonacci(num))