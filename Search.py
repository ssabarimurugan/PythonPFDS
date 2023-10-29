def Search(arr, x):
    
    for num in arr:
        if num == x:
            print("Found")
            return

    print("Not Found")

def BinarySearch(arr, x):  
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return True
 
    # If we reach here, then the element was not present
    return False

def main():
    arr = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    x = int(input("Enter the number to search: "))
    
    Search(arr, x)

    result = BinarySearch(arr, x)
    if result == True:
        print("Found")
    else:
        print("NotFound")


if __name__ == "__main__":
    main()
