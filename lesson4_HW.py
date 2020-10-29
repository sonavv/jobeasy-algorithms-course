##Enter a string of words separated by spaces.
##Find the longest word. (split / join methods)


def longest_word(str1):
    li = str1.split()
    x=[]
    for i in li:
        x.append(len(i))
    result = x.index(max(x))
    return li[result]
    
str1= input("Enter the string : ")
print(longest_word(str1))


##Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string, and words may be separated by several spaces).
##Make the string regular (delete all spaces at the beginning and end of the string, leave one space separating words).

s= input("Enter a sentence with spaces: ")
print("The sentence after removing spaces : ", ' '.join(s.split()))


