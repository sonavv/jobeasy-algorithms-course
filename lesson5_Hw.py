##When given a list, the program should return a list of all the elements that are below the arithmetical mean of the original list.
##The arithmetical mean is the sum of all elements divided by the number of elements.


def mean_list(list_1):
    n = len(list_1)
    mean = sum(list_1) / n
    print("Mean for the list is : ", mean)
    list_2 = []
    for i in range(n):
        if list_1[i] < mean:
           list_2.append(list_1[i])
    return list_2

list_1 = [5,5,2,0]
print(mean_list(list_1))

##When given a list of elements find the two lowest elements.
##They can be equal to each other or different.

def two_smallest(arr): 
  
    length = len(arr) 
    if length < 2: 
        print ("Invalid Input")
        return
  
    first = second = max(arr)
    for i in range(0, length):  
        if arr[i] < first and second == first:
            first = arr[i]
        elif (arr[i] < second and arr[i] != first): 
            second = arr[i]; 
    if (second == max(arr)): 
        print ("No second smallest element")
    else: 
        print ('The smallest element is',first,' second smallest element is',second)

arr = [0,1,2,2,1]
print(two_smallest(arr))

##Write a Python program to remove duplicates from a list.


def duplicate(a):
    dup_list = []
    uniq_list = []
    for x in a:
        if x not in dup_list:
            uniq_list.append(x)
            dup_list.append(x)
            uniq_list.sort()
    return uniq_list


a = [10,10,30,20,40,40,60,50,80,50,40]
print(duplicate(a))

##Given the triangle of consecutive odd numbers:

def sum_odd(n):
    list1 = []
    first_num = (n * n) - (n -1)
    while(n > 0):
        list1.append(first_num)
        first_num += 2
        n = n -1
    return sum(list1)

n = int(input("enter the number :"))
print(sum_odd(n))

