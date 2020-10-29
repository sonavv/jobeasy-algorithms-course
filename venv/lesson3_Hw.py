####Write a Python function, which will count how many times a character (substring) is included in a string. DON’T USE METHOD COUNT


##str1 = input("Enter the String: ")
##c = 0
##letter =input("Enter the letter to count in the string: " )
##for i in str1: 
##    if i == letter: 
##        c = c + 1
##   
##print ("The letter ",letter," in given string occurs : ", c,"time") 


##str1 = input("Enter the String: ")
##str2 = str1
####letter =input("Enter the letter to replace in the string: " )
##for i in str1: 
##    if i == str1:
##        str1[i] = 'o'        
##        
       
   


def decompress_string(string):
    result = ''
    char = ''
    count = ''
    s_len = len(string)

    for i in range(s_len):
        if string[i].isalpha():
            if count != '':
                result += char * (int(count) - 1)
                count = ''
            char = string[i]
            result += char
        else:
           count += string[i]
           if i == s_len - 1:
              result += char * (int(count)- 1)
    return result
            
    
print(decompress_string('a4b3c2'))
