#prog with strings:
#1 remove a character from string
str = input("please enter a string : ")
ch = input("please enter a character : ")
print(str.replace(ch,""))

#2 python prog count occurances of a charcter in a string
s = input("Please enter String : ")
char = input("Please enter a Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("Total Number of occurence of ", char, "is :" , count)

#3 anagram or not
str1=input("enter the first string:") #ex:arc=car,cat=act,cider=cried
str2=input("enter the second string:")
#converting both strings into lowercase
str1=str1.lower()
str2=str2.lower()
#check if length is same
if(len(str1)==len(str2)):
    #sort strings
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)
    #if sorted char arrays are same
    if(sorted_str1==sorted_str2):
        print(str1 +"and"+ str2 +"are anagram.")
    else:
        print(str1 + "and" + str2 + "are not anagram.")
else:
    print(str1 +"and" +str2 +"are not anagram.")

#4 palindrome or not
string=input(("enter a string:"))# ex-madam
if(string==string[::-1]):
    print("The string is palindrome")
else:
    print("Not a palindrome")

#5 write a python program to check if given character is vowel or consonant
character=input("enter a character:")
vowels=['a','e','i','o','u','A','E','I','O','U']
if character in vowels:
    print("The character  is a vowel!")
else:
    print("The character  is a consonant!")

#6 python program to print given charcter is digit or not
num= input("Enter a character : ")
if num >= '0' and num<= '9':
    print("Given Character ", num, "is a Digit")
else:
    print("Given Character ", num, "is not a Digit")

#7 Python code to check given character is digit or not using ‘isdigit()’ function
digit = input("Enter a character : ")
if(digit.isdigit()):
    print("The Given Character ", digit, "is a Digit")
else:
    print("The Given Character ", digit, "is not a Digit")

#8 Write a python program to replace string space with given character in Python.
string = input("enter string:")
space = "" #empty string
replace_with = input("enter char:")
for i in string:
    if i == " ": #if any space found in the string
        i = replace_with #replacing space with character
    space += i #concatenating each character with the string without space
print(space)

#9 Python code to replace the string space with given character
string = input("Enter a String : ")
result = ''  #empty string
c = input("Enter a Character : ")
for i in string:  #iterating using for loop
        if i == ' ':  #if any space found in the string
            i = c   #replacing space with character
        result += i   #concatenating each character of the string without space
print(“String after removing space with t = ”,result)

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

