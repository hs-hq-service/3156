import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

factorial(int(sys.argv[1]))
