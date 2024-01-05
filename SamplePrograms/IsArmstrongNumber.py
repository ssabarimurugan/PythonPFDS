def IsArmstrong(number, order):
    sum = 0
    for num in str(number):
        sum += pow(int(num), int(order))
    if sum == int(number) :
        print(str(number) + " is armstrong number")
    else :
        print(str(number) + " is not armstrong number")

if __name__ == "__main__":
    while True:
         number = input("Enter the number to be validated:\n")
         if number.isnumeric() :
             break   
    while True:
         order = input("Enter the order:\n")
         if order.isnumeric() :
             break        
    IsArmstrong(number, order)
