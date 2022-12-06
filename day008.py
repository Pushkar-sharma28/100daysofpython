def greet_with_name(name):
    print(f"hey {name}")
    print(f"how are u {name}")


#function with multiple input
'''
  def(var1,var2...varn):
  
'''

#function with multiple values but we don't have
# to take account of which values goes to which parameter of the function
'''
def fnname(var1,var2,var3):
    do something
    
calling
fnname(var2="name",var1="value",var3="quantity")

'''
'''spell=input("enter the name")
greet_with_name(spell)
'''

def encrypt(text,shift):
    cypher_text=""
    for i in range(0,len(text)):
        new_letter=(ord(text[i])-65+shift)%26
        new_letter=chr(new_letter)
        cypher_text+=new_letter
    print(cypher_text)


eorn=input("Type encode to encrypt,type decode to decrypt")
value=""
if eorn =='e':
       text=input("Text your message:")
       shift=int(input("Enter the shift number"))
       encrypt(text,shift)
