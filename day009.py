#dictionary : {key:value} same as maps

prog={
    "bug":"stops program to run the way it should be",
    "function": "a price of code that can be used repetitively just by using that funciton"
}
#to print the value of a particular key
#if the key is not present it shows the error
print(prog["bug"])

#adding new_items to dictionary
prog["latest_edit"]="this is the new edit"

#looping through dict
'''for i in prog:
    print(i)
output:
bug
function
latest_edit
'''

#to loop through the whole dict
for i in prog:
    print(i)
    print(prog[i])


#Nesting list - list inside list
'''
Examples:
dict={1:"this",2:"that",3:"those"}
dict1={4:"anything"}
list=[dict,dict1]

list=[[1,2,3],[4,5,6]]
'''

