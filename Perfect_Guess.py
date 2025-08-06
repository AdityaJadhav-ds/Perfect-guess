import random 

cam = random.randint(1 , 100)


guess = 0
you = -1 
while ( you != cam )  :
    you = int ( input ("Guess the number : ")) 
    if you < cam : 
        print ( " Enter Higher number please!!! ")
        guess += 1

      
    elif you > cam : 
        print ( " Enter Lower number please!!! ")
        guess += 1

guess += 1
print (f"\nCongratulation You Chose the correct number : { you } \nYou Take the {guess} guesses \nNow You Friebds Turn...")


      
