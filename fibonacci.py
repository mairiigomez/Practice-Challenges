"""One of the greatest discovers in math numbers of fibonacci and golden ratio 
1,1,2,3,5,8,13,21,34,55, etc. each number is the result of adding the two 
previous to it the fibonacci number divide it by the previous will be 1.6... 

With Fibonacci Sequence we practice recursivity
"""

def fibonacci(n):
    # Define the base case
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number: "))
print(fibonacci(n))

    