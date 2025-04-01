#9- Rock,Paper,scissor

import random
def play_game():
    options=['rock','paper','scissor']
    #Get User Choice
    user_choice=input("Chosse Rock,Paper or Scissor:").lower()
    #Check user input vaild or not
    if user_choice not in options:
        print("Invalid Choice")
    else:
        computer_choice= random.choice(options)
            # Show choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        if user_choice==computer_choice:
            print("It's a Tie!")
        elif(
            (user_choice=="rock" and computer_choice=="scissor"),
            (user_choice=="scissor" and computer_choice=="paper"),
            (user_choice=="paper" and computer_choice=="rock")
            ):
            print("You Win !")
        else:
            print("You loss!")
while True:
    play_game()
     # Ask if the user wants to play again
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break