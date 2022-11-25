#Datatypes:
#string

print("hello"[0])
#prints h since this can be taken as a string as well

#integer
print(123+234)
#large numbers can be written as 123_456

#float
3.14159

#boolean
True
False

#type error
if the variable is not of the type that we are trying to use

ex :
x=len(input())
print("your name is "+x+"sharma")
where x is a integer so it is an error

#check datatype of anything
print(type(x))
will print int


#type conversion
str=input()
str=int(str)

'''operators:
  + , - , *, / , ** , %'''
  

#rounding off
print(round(2.453345,2))
#floor division - gives the answer in the integer form
print(type(8//3))

#some more maths operations
+=
-=

#f strings
str="pushkar"
print(f"your name is {str}")
#this was the most basic way of writing in f strings


#tip calculator
print("welcome to the tip calculator")
bill=int(input(print("What was the total bill")))
tip=int(input(print("What percentage tip would you like to give? 10,12 or 15?")))
count=int(input(print("how many people to split the bill?")))
dummy=bill+(bill*tip)/100
ans=round(dummy/count,2)
print(f"Each person should pay {ans}")

