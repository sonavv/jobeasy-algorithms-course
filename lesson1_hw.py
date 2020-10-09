##Sum of 3 modified
# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0


def sumdigit(n):
    sum = 0

    while(n>0):
        sum += int(n%10)
        n = int(n/10)

    return sum

n = int(input("enter the digits "))
print(sumdigit(n))


##Find max number from 3 values, entered manually from a keyboard


def max_num(list1):
    a = list1[0]
    for x in list1:
        if x > a:
            a = x
    return a

num1 = int(input( 'Enter the first number: '))
num2 = int(input( 'Enter the second number: '))
num3 = int(input( 'Enter the third number: '))

list1 = [num1, num2, num3]
print("The largest number is :", max_num(list1))

##Count odd and even numbers.  Count odd and even digits of the whole number. E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

def count_even_odd(n):
    even_count = 0
    odd_count = 0
    while n> 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 10
    return {
        'odd' : odd_count,
        'even' : even_count
        }

number = int(input(f" Enter a number : "))
print(count_even_odd(number))



             

