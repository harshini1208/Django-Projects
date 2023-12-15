#8 Write a python program to replace string space with given character in Python.
string = input("enter string:")
space = "" #empty string
replace_with = input("enter char:")
for i in string:
    if i == " ": #if any space found in the string
        i = replace_with #replacing space with character
    space += i #concatenating each character with the string without space
print(space)


#9 replace a string space with given character using replace()
s1=input('enetr your string')
s2=input('enetr your character to replace')
s3=s1.replace(' ',s2)
print(s3)

#10 Python code to convert lowercase character to uppercase character of string
str = input("Enter a String : ")
result_str = ''
for i in str:  # iterate through each letter/character from the string
    if i.islower():  # if lowercase
        i = i.upper()  # converting lowercase into uppercase letter
    result_str += i  # concatenating each character of the string without lowercase letter
print("String after converting lower case to upper :", result_str)

#11 Convert Lowercase vowels to Uppercase using replace() method
str = input("Enter a string: ")
vowels = "aeiou"
for char in str:
    if char in vowels:
        # convert the lowercase vowel to uppercase
        upper_char = char.upper()
        # replace the lowercase vowel with the uppercase vowel
        string = string.replace(char, upper_char)
print("Updated string:", string)

#12 Python code to remove vowels from the string
string = input("Enter a String : ")
result=''
for i in string:
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
     #seaching for vowels
        i = ''
    result += i #concatenating rest of string
print("String after removing the vowels :",result)

#13 count the occurences vowels or consonants in a string
string = input("Enter a String : ")
vowels = 0  #variable to count number of vowels
consonants = 0 #variable to count number of consonants
for i in string:  #string iteration
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):  #if character in string is vowel
        vowels+=1 #if vowel increment variable ‘vowel’ with one
    elif i.isalpha():  #checking if the character is alphabet
        consonants+=1  #if consonant increment variable ‘consonants’ with one
print("Vowels :",vowels,"Consonants:",consonants)

#14 python prog to print highest frequency of a charcater in a string
s1=input('enter your string')
h=0
s2=set(s1)
for ch in s2:
    if s1.count(ch) > h:
        h=s1.count(ch)
for ch in s2:
    if h==s1.count(ch):
        print('highest frequency of a character',ch)

#15 replace first occurence of vowel with '-' in a string

def replace_vowel(string):
    vowels = "AEIOUaeiou"
    for i in range(len(string)):
        if string[i] in vowels:
            string = string[:i] + '-' + string[i+1:]

            break
    return string

string = input("Please enter a string: ")
print(replace_vowel(string))

#16 python code to count  alphabets,special characters,digits in a string
string = input("Enter a String : ")
alphabets=0
digits=0
specialChars=0
for i in string:
  if i.isalpha():
    alphabets+=1
  elif i.isdigit():
    digits+=1
  else:
    specialChars+=1
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)

#17 remove all blank spaces from a string
#taking input from the user
string = input("Enter a String : ")
result=''
#iterating the string
for i in string:
    #if the character is not a space
    if i!=' ':
        result += i
print("String after removing the spaces :",result)

#18 python prog to concatenate two strings using join() method
str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
print("String after concatenation :","".join([str1, str2]))

#20 concatenating two strings
str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
str3 = str1 + str2
print("String after concatenation :",str3)

#21 python prog to remove repeated character
#using list and join()
def remove_duplicates(s):
    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)
    return "".join(unique_chars)
string = input("Please Enter a string: ")
print(remove_duplicates(string))

#22 calculate sum of integers in a string
s=input("Enter the string:")
sum=0
for i in s:
    if i.isdigit():
     sum=sum+int(i)
     print(sum)

#23 repeated charcter in a string
str=input("enter string :")
p=""
for char in str:
    if char not in p:
        p=p+char
print(p)

#24 copy one string to another string
string = input("Please Enter a string: ")    #using slice operator-it can perform copy of original string to new string
new_string = string[:]
print("New String After Copy:", new_string)

#method 2:
string = input("Please Enter a string: ")
new_string = ""
for char in string:
    new_string += char
print("New String:", new_string)

#25 sorting of string character in ascending order
string = input("Enter the string : ")
strList=list(string)
new_string=''.join(sorted(strList))
print("String Sorted in ascending order :",new_string)

#26 sort a string in descending order
string = input("Enter the string : ")
strList=list(string)
sortedString=''.join(sorted(strList, reverse =True))
print("String Sorted in ascending order :", sortedString)
