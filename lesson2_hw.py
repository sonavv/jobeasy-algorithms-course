# Fibonacci Series using Dynamic Programming  

n = int(input(" Enter the element to find the value in fibonacci : "))
        
def fibonacci(n):  
      
      
    Fiblist = [0, 1]  

    while len(Fiblist) < n + 1:  
        Fiblist.append(0)  
      
    if n <= 1:  
        return n  
    else:  
        if Fiblist[n - 1] == 0:  
            Fiblist[n - 1] = fibonacci(n - 1)  
  
        if Fiblist[n - 2] == 0:  
            Fiblist[n - 2] = fibonacci(n - 2)  
              
    Fiblist[n] = Fiblist[n - 2] + Fiblist[n - 1]  
    return Fiblist[n]  
      
print(fibonacci(n))


##Zeros not for Heros
##Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of them. Only the ending ones.

def removeZeros(number):
    
    if number == 0 :
        return 0


    while number%10 == 0:
        number /= 10
    return number

number = int(input("Enter a number to remove zeros: "))
print(round(removeZeros(number)))


##Digital root is the recursive sum of all the digits in a number.


def sumdigit(n):
    sum = 0

    while(n>0):
        sum += int(n%10)
        n = int(n/10)
    if sum <= 9:
       return sum
    return sumdigit(sum)
        

n = int(input("enter the digits for recursive sum"))
print(sumdigit(n))


