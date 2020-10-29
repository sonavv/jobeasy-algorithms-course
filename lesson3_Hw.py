####Write a Python function, which will count how many times a character (substring) is included in a string. DON’T USE METHOD COUNT


str1 = input("Enter the String to count a character from: ")
c = 0
letter =input("Enter the character to be counted: " )
for i in str1: 
    if i == letter: 
        c = c + 1
   
print ("The character ",letter," in given string occurs : ", c,"times") 



       
##Find and replace a substring in a string for another substring. User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE


def replace(string_1, old_substr, new_substr):
    len_old_string = len(old_substr)
    index = string_1.find(old_substr)
    while index > -1:
        string_1 = f'{string_1[:index]}{new_substr}{string_1[index + len_old_string:]}'
        index = string_1.find(old_substr)
    return string_1

##print(replace('replace test code', 'test', 'best'))
##print(replace('This is best', 'best', 'test'))

string_1 = input("Enter the whole string with substring that needs to be replaced: ")
old_substr = input("Enter the substring to be replaced: ")
new_substr = input("Enter the new substring: ")
print("Before Replacing : ", string_1 )
print("After Replacing :", replace(string_1, old_substr, new_substr))

 
##Write a function for decompressing string “a4b3c2d”

def decomp(string):
    len_str = len(string)
    result = ''
    count = ''

    for i in range(len_str):
        if string[i].isalpha():
            char = string[i]
            result += char
            count = ''
        else:
             count += string[i]
             result += char * (int(count)- 1)
    return result
print("The string after decompressing is: ", decomp('a4b3c2d'))


##Recursion for Factorial

def factorial(number):
    if number == 1:
        return 1
    else:
        return (number * factorial(number-1))

number = int(input("Enter a number to find factorial : "))
print("The factorial of", number, "is", factorial(number))

### Recursion on Fib

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

num = int(input("Enter the number to find fibnocci series: "))
for i in range(num):
    print(fibo(i))

##Recursion for  digital root

def sumdigit(n):
    sum = 0

    while(n>0):
        sum += int(n%10)
        n = int(n/10)
        if sum > 10:
            sum = sumdigit(sum)
    return sum

n= int(input("Enter the number to find digital root of: "))
print("The digital root of the given number is : ",sumdigit(n))








