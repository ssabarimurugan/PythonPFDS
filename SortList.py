def SortList(lst):
    lst.sort()
    print(lst)


if __name__ == "__main__":
    lst = []
    
    n =  int(input("Enter the number of elements in the array:"))
    
    for i in range(0, n):
        ele = input()
        lst.append(ele) 
    
    SortList(lst)
