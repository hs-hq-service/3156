# factorial.py
#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative-integer>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: argument must be an integer")
        sys.exit(1)
    try:
        print(factorial(n))
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
