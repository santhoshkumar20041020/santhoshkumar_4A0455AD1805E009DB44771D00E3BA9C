# Implement a recursive function to calculate the factorial of a given number

def factorial(n):
  if n==0:
      return 1
  else:
      return n* factorial(n-1)
print(format("FACTORIAL",'^50'))
n=int(input("Enter a number to find factorial:"))
print("Factorial of given number ",n,"is:",factorial(n))