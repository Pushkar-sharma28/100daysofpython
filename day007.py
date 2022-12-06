import random
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)

dummy=[]
for i in range(0,len(chosen_word)):
      dummy+="_"
value="_"
life=5
winornot=1
while(value in dummy):
      print(dummy)
      letter=input("Guess the letter")
      if letter in chosen_word:
          print("u guessed it right")
          for i in range(0,len(chosen_word)):
              if(chosen_word[i]==letter):
                  dummy[i]=letter
      else :
          print("u guessed it wrong")
          life-=1
          print(life)

      if(life==0):
         print("you lost the game sir")
         winornot=0
         break

if(winornot):
    print("oww u won the game")
else:
    print()