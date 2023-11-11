# write a prgrom to print "hello world"

# As we learned in the introduction to this challenge, the winner of the game is determined by three simple rules:

    # Rock beats scissors.
    # Scissors beat paper.
    # Paper beats rock.

import random

# Define the options
options = ["rock", "paper", "scissors"]

# Define the function to determine the winner
def determine_winner(option1, option2):
    if option1 == option2:
        return "tie"
    elif option1 == "rock" and option2 == "scissors":
        return "player 1 wins"
    elif option1 == "paper" and option2 == "rock":
        return "player 1 wins"
    elif option1 == "scissors" and option2 == "paper":
        return "player 1 wins"
    elif option1 == "rock" and option2 == "paper":
        return "player 2 wins"
    elif option1 == "paper" and option2 == "scissors":
        return "player 2 wins"
    else:
        return "player 1 wins"

# Define the main function
def main():
    # Print the game instructions
    print("Welcome to the rock-paper-scissors game!")
    print("Here are the rules:")
    print("Rock beats scissors.")
    print("Scissors beat paper.")
    print("Paper beats rock.")
    print("--------------------------------------------------")

    # Loop until the game is over
    while True:
        # Get the player's choice
        player_choice = input("Player 1, please choose rock, paper, or scissors: ").lower()

        # Check if the player's choice is valid
        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get the computer's choice
        computer_choice = random.choice(options)

        # Determine the winner
        winner = determine_winner(player_choice, computer_choice)

        # Print the results
        print("Player 1 chose:", player_choice)
        print("Computer chose:", computer_choice)
        print("--------------------------------------------------")

        # Check if the game is over
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player 1 wins":
            print("Player 1 wins!")
        else:
            print("Computer wins!")
            break

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again!= "y":
            break

# Call the main function
if __name__ == "__main__":
    main()