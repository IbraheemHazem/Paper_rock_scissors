import random
print("Welcome to 'paper,rock,scissors' game!")

while True:
    PlayerChoice = input("Choose 'p' for paper or 'r' for rock or 's' for scissors to initiate:\n").lower()

    Pc_Options = ["p", "r", "s"]
    Pc_Choice = random.choice(Pc_Options)

    if PlayerChoice not in Pc_Options:
        print("Invalid choice, make sure you typed the right order or you will be 'Out Of Order'.")

    else:
        print(f"Your choice:{PlayerChoice}")
        print(f"Mine:{Pc_Choice}")

        if PlayerChoice == Pc_Choice:
            print("So it is a tie! cheers to both of us!")
        elif PlayerChoice == 'p' and Pc_Choice == 'r' or PlayerChoice == 'r' and Pc_Choice == 's' or PlayerChoice == 's' and Pc_Choice == 'p':
            print("Then you win! Congrats(baring my teeth)!")
        else:
            print("Then I win! Now you have to pay me 13 USD that I Paid you earlier!")
            
            Joke = input("Did you accept the joke I said to you?![y/n]\n")
            if Joke == ("y").lower():
                print("Great! You are funny and smart too.")
            else:
                print("Then bang your head against the toughest brick wall and let us see what happens")

        continue_playing = input("Do you want to continue?[y/n]\n").lower()
        if continue_playing != ('y'):
            break






import random

print("Welcome to the 'Rock, Paper, Scissors' game!")

while True:
    player_choice = input("Choose 'p' for paper, 'r' for rock, or 's' for scissors to initiate:\n").lower()

    pc_options = ["p", "r", "s"]
    pc_choice = random.choice(pc_options)

    if player_choice in pc_options:
        print(f"Your choice: {player_choice}")
        print(f"My choice: {pc_choice}")

        if player_choice == pc_choice:
            print("It's a tie! Cheers to both of us!")
        elif (player_choice == 'p' and pc_choice == 'r') or (player_choice == 'r' and pc_choice == 's') or (player_choice == 's' and pc_choice == 'p'):
            print("You win! Congrats (bearing my teeth)!")
        else:
            print("I win! Now you owe me $13 for that joke.")

            joke_accepted = input("Did you accept the joke I said to you? (y/n): ").lower()
            if joke_accepted == 'y':
                print("Great! You are funny and smart too.")
            else:
                print("Then bang your head against the toughest brick wall and let us see what happens.")

        continue_playing = input("Do you want to continue? (y/n): ").lower()
        if continue_playing != 'y':
            break

    else:
        print("Invalid choice. Make sure you typed the right option: 'p' for paper, 'r' for rock, or 's' for scissors.")





import random

print("Welcome to the 'Rock, Paper, Scissors' game!")

while True:
    player_choice = input("Choose 'p' for paper, 'r' for rock, or 's' for scissors to initiate:\n").lower()
    pc_choice = random.choice(["p", "r", "s"])

    if player_choice not in {"p", "r", "s"}:
        print("Invalid choice. Choose 'p' for paper, 'r' for rock, or 's' for scissors.")
        continue

    print(f"Your choice: {player_choice}\nMy choice: {pc_choice}")

    result = "It's a tie! Cheers to both of us!" if player_choice == pc_choice else "You win! Congrats (bearing my teeth)!" if (player_choice == 'p' and pc_choice == 'r') or (player_choice == 'r' and pc_choice == 's') or (player_choice == 's' and pc_choice == 'p') else f"I win! Now you owe me $13 for that joke.\n{'Great! You are funny and smart too.' if input('Did you accept the joke I said to you? (y/n): ').lower() == 'y' else 'Then bang your head against the toughest brick wall and let us see what happens.'}"

    print(result)
    
    if input("Do you want to continue? (y/n): ").lower() != 'y':
        break







import random

# Welcome message
print("Welcome to the 'Rock, Paper, Scissors' game!")

# Game loop
while True:
    # Player makes a choice
    player_choice = input("Choose 'p' for paper, 'r' for rock, or 's' for scissors to initiate:\n").lower()
    
    # Computer randomly chooses 'p', 'r', or 's'
    pc_choice = random.choice(["p", "r", "s"])

    # Check if the player's choice is valid
    if player_choice not in {"p", "r", "s"}:
        print("Invalid choice. Choose 'p' for paper, 'r' for rock, or 's' for scissors.")
        continue  # Go back to the start of the loop if the choice is invalid

    # Display player and computer choices
    print(f"Your choice: {player_choice}\nMy choice: {pc_choice}")

    # Determine the game result
    result = (
        "It's a tie! Cheers to both of us!" if player_choice == pc_choice
        else "You win! Congrats (bearing my teeth)!" if (player_choice == 'p' and pc_choice == 'r') or (player_choice == 'r' and pc_choice == 's') or (player_choice == 's' and pc_choice == 'p')
        else f"I win! Now you owe me $13 for that joke.\n{'Great! You are funny and smart too.' if input('Did you accept the joke I said to you? (y/n): ').lower() == 'y' else 'Then bang your head against the toughest brick wall and let us see what happens.'}"
    )

    # Display the result
    print(result)

    # Ask if the player wants to continue
    if input("Do you want to continue? (y/n): ").lower() != 'y':
        break  # Exit the loop if the player doesn't want to continue