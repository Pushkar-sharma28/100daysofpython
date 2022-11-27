
import random
#for loop in python

#loop on list
fruits=["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)


#maximum in the array
'''
maxi=-100
for i in student_scores:
    if(maxi<i):
        maxi=i
print("The highest score in the class is: "+str(maxi))
#using functions:
print(max(student_list)) 
'''


#range functions: range(start,end,jump)

sum=0
for i in range(0,100+1,1):
    sum+=i
print(sum)
'''
#fizzbuzz
n=int(input())
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("Fizz")
    else :
        print(i)
'''
#Password generator
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

passw=[]
for i in range (0,3):
    passw.append(random.choice(DIGITS))
    passw+=random.choice(LOCASE_CHARACTERS)
    passw+=random.choice(UPCASE_CHARACTERS)
    passw+=random.choice(SYMBOLS)

random.shuffle(passw)
password=""
for i in passw:
    password+=i
print(password)