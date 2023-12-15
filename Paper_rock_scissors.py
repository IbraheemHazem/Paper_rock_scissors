import random

# Welcome message to the game
print("Welcome to 'paper, rock, scissors' game!")

# Main game loop
while True:
    # Get user input for choice (paper, rock, or scissors)
    PlayerChoice = input("Choose 'p' for paper, 'r' for rock, or 's' for scissors to initiate:\n").lower()

    # Options for the computer (randomly chosen)
    Pc_Options = ["p", "r", "s"]
    Pc_Choice = random.choice(Pc_Options)

    # Check if the user's choice is valid
    if PlayerChoice in Pc_Options:
        # Display the user and computer choices
        print(f"Your choice:{PlayerChoice}")
        print(f"Computer's choice:{Pc_Choice}")

        # Check the outcome of the game
        if PlayerChoice == Pc_Choice:
            print("So it is a tie! Cheers to both of us!")
        elif PlayerChoice == 'p' and Pc_Choice == 'r' or PlayerChoice == 'r' and Pc_Choice == 's' or PlayerChoice == 's' and Pc_Choice == 'p':
            print("Then you win! Congrats (baring my teeth)!")
        else:
            print("Then I win! Now you have to pay me 13 USD that I paid you earlier!")

            # Ask the user if they accepted the joke
            Joke = input("Did you accept the joke I said to you? [y/n]\n").lower()
            if Joke == ("y").lower():
                print("Great! You are funny and smart too.")
            else:
                print("Then bang your head against the toughest brick wall and let us see what happens")

        # Ask the user if they want to continue playing
        continue_playing = input("Do you want to continue? [y/n]\n").lower()
        if continue_playing != ('y'):
            break

    else:
        # Display an error message for an invalid choice
        print("Invalid choice, make sure you typed the right order or you will be 'Out Of Order'.")