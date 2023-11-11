# write a prgrom to print "hello world"

# As we learned in the introduction to this challenge, the winner of the game is determined by three simple rules:

    # Rock beats scissors.
    # Scissors beat paper.
    # Paper beats rock.

import random

# Define the game options
options = ["rock", "paper", "scissors"]

# Define the function to play the game
def play_game():
    # Initialize the score
    score = {"wins": 0, "rounds": 0}

    # Loop until the minigame is terminated
    while True:
        # Get the player's choice
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        # Check if the player's choice is valid
        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get the computer's choice
        computer_choice = random.choice(options)

        # Print the player's and computer's choices
        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            score["wins"] += 1
        elif player_choice == "paper" and computer_choice == "rock":
            print("You win!")
            score["wins"] += 1
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            score["wins"] += 1
        else:
            print("Computer wins!")

        # Increment the round count
        score["rounds"] += 1

        # Ask the player if they want to continue
        if input("Do you want to continue? (y/n): ").lower()!= "y":
            break

    # Print the final score
    print("Final score:", score["wins"], "wins", score["rounds"], "rounds")

# Call the play_game function to start the game
play_game()