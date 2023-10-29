import math

def PrimeFactors(n):
    while n % 2 == 0 :
        print(2)
        n = n // 2
    
    for i in range(3, int(math.sqrt(n)+1), 2) :
        while n % i == 0 :
            print(i)
            n = n // i

    if (n > 2):
        print(n)

if __name__ == "__main__":
    while True:
         number = input("Enter a number:\n")
         if number.isnumeric() :
             break          
    PrimeFactors(int(number))
