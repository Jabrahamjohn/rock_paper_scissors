import random

def play_round(player_choice, computer_choice):
    """
    Function to determine the outcome of a single round of Rock, Paper, Scissors game.
    
    Args:
    - player_choice (str): The player's choice ('rock', 'paper', or 'scissors').
    - computer_choice (str): The computer's choice ('rock', 'paper', or 'scissors').
    
    Returns:
    - int: 0 if it's a tie, 1 if the player wins, -1 if the computer wins.
    """
    outcomes = {'rock': {'rock': 0, 'paper': -1, 'scissors': 1},
                'paper': {'rock': 1, 'paper': 0, 'scissors': -1},
                'scissors': {'rock': -1, 'paper': 1, 'scissors': 0}}
    
    return outcomes[player_choice][computer_choice]

def validate_choice(choice):
    """
    Function to validate the player's choice.
    
    Args:
    - choice (str): The player's input.
    
    Returns:
    - str or None: Validated choice ('rock', 'paper', or 'scissors') or None if invalid.
    """
    valid_choices = ['rock', 'paper', 'scissors']
    if choice.lower() in valid_choices:
        return choice.lower()
    else:
        return None

def main():
    """
    Main function to run the Rock, Paper, Scissors game.
    """
    player_score = 0
    computer_score = 0
    play_again = True
    
    print("Welcome to Rock, Paper, Scissors game!")
    
    while play_again:
        print("\nMake your choice: rock, paper, or scissors (type 'quit' to exit)")
        player_choice = input("> ")
        
        if player_choice.lower() == 'quit':
            break
        
        player_choice = validate_choice(player_choice)
        
        if player_choice is None:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")
        
        result = play_round(player_choice, computer_choice)
        
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print("You win!")
            player_score += 1
        elif result == -1:
            print("Computer wins!")
            computer_score += 1
        
        print(f"Score - You: {player_score} | Computer: {computer_score}")
        
        print("\nDo you want to play again? (yes/no)")
        play_again_input = input("> ").lower()
        
        if play_again_input != 'yes':
            play_again = False
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
