import random
print("----------WELCOME TO THE GAME ROCK,PAPER,SCISSOR----------")
print("----------FIVE CHANCES ARE THERE-----------------")
print("----------Enter From Rock,Paper,Scissor--------")
user_point=0
computer_point=0
chance=0
while(chance!=5):
    user_input = input("Enter Your Choice:-").lower()
    computer_input = ["Rock","Scissor","Paper"]
    computer_choice = random.choice(computer_input).lower()
    
    if user_input==computer_choice:
        print("----------Both Have Same Input-------------")
    else:
        if user_input=='rock' and computer_choice=='scissor' or user_input=='scissor' and computer_choice=='paper' or user_input=='paper' and computer_choice=='rock':
            print("------------User Wins Point-------------")
            user_point+=1
        elif user_input=='scissor' and computer_choice=='rock' or user_input=='paper' and computer_choice.lower()=='scissor' or user_input=='rock' and computer_choice=='paper':
            print("-------Computer Wins Point---------")
            computer_point+=1
        else:
            print("--------Invalid Input Please Try Again-----------")
    chance+=1
print("---------------FINAL SCORECARD-------------")
if user_point==computer_point:
    print("-----------GAME TIE---------------")
    print("User Score:",user_point)
    print("Computer Score:",computer_point)
elif user_point>computer_point:
    print("-----------USER WINS--------------")
    print("User Score:",user_point)
else:
    print("-----------COMPUTER WINS-----------")
    print("Computer Score:",computer_point)