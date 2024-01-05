def FindDuplicates(lst):
    freq = {}       
    for num in lst:
        if freq.get(num) is not None:
            freq[num] += 1
        else:
            freq[num] = 1

    for x in freq :
        if freq[x] > 1:
            print('{} is duplicated {} times'.format(x, freq[x]))


if __name__ == "__main__":
    lst = []
    
    n =  int(input("Enter the number of elements in the array:"))
    
    for i in range(0, n):
        ele = int(input())
        lst.append(ele) 
    
    FindDuplicates(lst)
