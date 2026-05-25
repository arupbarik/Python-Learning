print("Recursion")

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))
# it is for check the limit of recursion
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000) # this code extend the calls to 2000.