#1 python program to print Prime number')
num=int(input('enter your number'))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print('prime number' if (count==2) else ('not prime'))


#2 python prog to print reverse of a number
num=int(input('enter your number'))
res=0
while(num!=0):
    rem=num%10
    res=res*10+rem
    num=num//10
print(res)

#3 python prog to print amstrong no or not
num=int(input('enter your number'))
sum=0
copy=num
p=len(str(num))
while(num!=0):
    rem=num%10
    sum+=rem**p
    num=num//10
print('armstrong' if sum==copy else ('not armstrong'))


#3 python program to print fibonocci numbers using iterative method
num=int(input('enter your number of fabnoccis series'))
n1,n2=0,1
for i in range(num+1):
    if i<2:
        print(i)
    else:
        print(n1+n2)
        n1,n2=n2,n1+n2


#4 fibonocci number using recursive function
def fab(n1,n2,num):
    if num==0:
        return
    print(n1+n2)
    return fab(n1=n2,n2=n1+n2,num=num-1)
num=int(input('enter number of fabnoccis seeris'))
print(0)
print(1)
fab(n1=0,n2=1,num=num-2)


#5 pallindrome  not using recursive fn
num=int(input('enter your number '))
rev=0
copy=num
while num!=0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print('palindrome' if num==copy else ('not palindrome'))



#6 pallindrome using recursion
def pal(rev,num,copy):
    if num==0:
        return 'palindrome' if rev==copy else ('not palindrome')
    return pal(rev=(rev*10)+num%10,num=num//10,copy=copy)
num=int(input('enter your number '))
print(pal(0,num,num))


#7 prog to find highest among numbers
n1=int(input('enter number 1'))
n2=int(input('enter number 2'))
n3=int(input('enter number 3'))
h=0
for i in [n1,n2,n3]:
    if i>h:
        h=i
print(h)


#8check the number is binary or not
num=int(input('enter number 1'))
while(num!=0):
    x=num%10
    if x!=0 and x!=1:
        print('not binary number')
        break
    else:
        num=num//10


#9 find sum of digits using recursive
def re(sum,num):
    if num==0:
        return ('sum of the digits is',sum)
    return re(sum=sum+num%10,num=num//10)
num=int(input('enter your number'))
print(re(0,num))


#10 swap two numbers without using third variable
n1=int(input('enter number 1'))
n2=int(input('enter number 2'))
print('numbers before swapping',n1,n2)
n1,n2=n2,n1
print('swapped numbers= ',n1,n2)


#12 swap two numbers using third variable
n1=int(input('enter number 1'))
n2=int(input('enter number 2'))
print('numbers before swapping',n1,n2)
n3=n1
n1,n2=n2,n3
print('swapped numbers= ',n1,n2)


#13 print prime factors of a given number
def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return (True if (count==2) else False)

num=int(input('enter your number'))
for i in range(1,num+1):
    if num%i==0 and prime(i):
        print(i)

#14 sum of number without using arthematic operator
n1=int(input('enter number 1'))
n2=int(input('enter number 2'))
print(sum([n1,n2]))

#15 check number is a perfect number or not
n1=int(input('enter your number'))
sum=0
for i in range(1,n1):
    if n1%i==0:
        sum+=i
if sum==n1:
    print('perfect num')
else:
    print('not perfect ')


#16 average of givem num'
numbers = [1, 2, 34, 56, 7, 23, 23, 12, 1, 2, 3, 34, 56]
sumOfNums = 0
count = 0
for number in numbers:
    sumOfNums += number
    count += 1
average = sumOfNums / count
print("The list of numbers is:", numbers)
print("The average of all the numbers is:", average)

#17 factorial of given num
n1=int(input('enter your number'))
res=1
for i in range(1,n1+1):
    res*=i
print(res)


#18 factorial of given num:
def fact(res,n):
    if n==0:
        return res
    return fact(res=res*n,n=n-1)
n1=int(input('enter your number'))
print(fact(1,n1))


#19square root of a givn num')
import math
n1=int(input('enter your number'))
print(math.sqrt(n1))

#20 convert decimal to binary
n1=int(input('enter ypour decimal num'))
rev=0
n=1
while n1!=0:
    rem=n1%2
    rev=rev+rem*n
    n1//=2
    n*=10
print(rev)
