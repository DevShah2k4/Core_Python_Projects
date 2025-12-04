import random
#This is Colour Guessing Game in which user guess a colour name and computer also take a colour name 
#if both mathches then user get a point other wise computer get a point
user_point = 0
computer_point = 0
chance = 0
print("---------------PLEASE SELECT COLOUR NAME FROM RAINBOW COLOURS-------------------")
print("---------------COLOUR NAMES----------------------------------------------------- \n1)RED \n2)YELLOW \n3)VIOLET \n4)GREEN \n5)ORANGE \n6)BLUE \n7)INDIGO")
print("---------------FIVE CHANCES ARE THERE-------------------------------------------")
while(chance!=5):
    user_colour = input("Enter Colour Name:-").lower()
    computer_input = ["red","yellow","violet","orange","green","blue","indigo"]
    computer_choice = random.choice(computer_input).lower()
    if user_colour in computer_input:
        if user_colour==computer_choice:
            print("-------------GUESS COLOUR IS RIGHT------------")
            user_point+=1
        elif user_colour != computer_choice:
            print("------------GUESS COLOUR IS WRONG-------------")
            computer_point+=1
    else:
        print("------------Invalid Input Please Try Again-----------------")
    chance+=1
print("--------------------FINAL SCORECARD----------------")
if user_point>computer_point:
    print("-----------------USER WINS---------------------")
    print("USER SCORE:",user_point)
else:
    print("-----------------COMPUTER WINS-----------------")
    print("COMPUTER SCORE:",computer_point)