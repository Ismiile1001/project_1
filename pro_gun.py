import random
# choice korte hobe 
computer_choice = random.choice([-1,1,0])
my_choice = input("Enter your choice :")


# dictionary 

game_choices = {
    "r": -1,
    "p": 1,
    "s": 0
} 



# create a dictionary for reverse 
reverse_choices = {
    -1: "Rock",
    1: "Paper",
    0: "Scissors"
}


# create a funtion for the game (you )
you = game_choices[my_choice]



# print 
print(f"my choice {reverse_choices[you] } \n computer choice  {reverse_choices[computer_choice]}")





# write all condition using the nasted if else 
if my_choice == computer_choice:
    print("It's a tie ")
else:
    if (my_choice == -1 and computer_choice == 1) or (my_choice == 1 and computer_choice == 0) or (my_choice == 0 and computer_choice == -1):
        print("You win!")
    else:
        print("computer win ")  


'''
best_logic -

if(computer_choice - you == -1)or (computer_choice - you == 2):
    print("You lose!")

    else:
    print("You win!")


'''     


