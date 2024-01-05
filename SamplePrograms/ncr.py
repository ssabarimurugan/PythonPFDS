import math

def ncr(n, r):
    print(factorial(n) / (factorial(r) * factorial(n-r)))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    while True:
         n = input("Enter the value of n:")
         if n.isnumeric() :
             break   
    while True:
         r = input("Enter the value of r:")
         if r.isnumeric() :
             break         
    ncr(int(n), int(r))
