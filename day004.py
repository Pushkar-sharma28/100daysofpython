#random module
#uses pseudo random generator

import random

#generate a random number using randint(a,b)
c=random.randint(1,10)
print(c)

#how to make a module just make a normal python file and
#make some funcitonality in that now call that file by this
# import file_name.py and functionalities can be used like
# my_module.pi

#random() this funciton generates a number between 0 to 1

random_float =random.random()
print(random_float)

random_float * 5

#python list data structure
list=["puskar","sharma",9]
#indexing and functions
''' 
append
remove 
pop
random.choice(names) where names is a list
'''

#nested list
fruit=["apple","banana"]
vegetables=["spinach","tomato"]
lsit=[fruit,vegetables]


#2-d lists
map=[[1,2,3],[4,5,6],[7,8,9]]
for i in map:
    print(i)

#rock paper scissors game:

rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves=[rock,paper,scissors]

n=int(input("Choose any of the three moves \n 1 for rock"
           "\n 2 for paper \n 3 for scissors "))
comp=random.randint(0,2)
if(n==1):
    if(comp==1):
        print("draw")
    elif(comp==2):
        print("You loss")
    elif(comp==3):
        print("Yow win")
elif(n==2):
    if (comp == 1):
        print("win")
    elif (comp == 2):
        print("draw")
    elif (comp == 3):
        print("loss")
elif(n==3):
    if (comp == 1):
        print("win")
    elif (comp == 2):
        print("loss")
    elif (comp == 3):
        print("draw")

