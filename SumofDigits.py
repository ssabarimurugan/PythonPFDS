def FindSum(number):
    sum = 0
    for num in str(number):
        sum += int(num)
    print(sum)


if __name__ == "__main__":
    while True:
         number = input("Enter a number:\n")
         if number.isnumeric() :
             break          
    FindSum(number)



