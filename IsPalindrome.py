def IsPalindrome(inputString):
    strLen = len(inputString)
    isPalindrome = False
    for i in range(strLen):
        if inputString[i] == inputString[strLen - i - 1] :
            if (2 * (i + 1)//strLen >= 1) :
                isPalindrome = True
                break
            else :
                continue
        else :
            break

    if isPalindrome :
        print(inputString + " is a palindrome")
    else :
         print(inputString + " is not a palindrome")

if __name__ == "__main__":
    inputString = input("Enter the string to be validated:\n")       

    IsPalindrome(inputString)
