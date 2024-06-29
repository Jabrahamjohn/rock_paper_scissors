# the rock paper scissors game
"""
Rock beats scissors
Scissors beats paper
paper beats rock
"""
import random

def mode():
    print("Welcome to the Rock Paper Scissors Game")
    print("Choose your mode")
    print("1. Player vs Computer")
    print("2. Computer vs Computer")
    print("3. player vs player")
    print("4. Exit")
    mode = input("Enter your choice: ")
    return mode

def player_vs_computer():
    print("Player vs Computer")
    player = input("Enter your choice: ")
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer choice: {computer}")
    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins")
        else:
            print("Computer wins")
    elif player == "scissors":
        if computer == "paper":
            print("Player wins")
        else:
            print("Computer wins")
    elif player == "paper":
        if computer == "rock":
            print("Player wins")
        else:
            print("Computer wins")
    else:
        print("Invalid choice")

def computer_vs_computer():
    print("Computer vs Computer")
    computer1 = random.choice(["rock", "paper", "scissors"])
    computer2 = random.choice(["rock", "paper", "scissors"])
    print(f"Computer1 choice: {computer1}")
    print(f"Computer2 choice: {computer2}")
    if computer1 == computer2:
        print("It's a tie")
    elif computer1 == "rock":
        if computer2 == "scissors":
            print("Computer1 wins")
        else:
            print("Computer2 wins")
    elif computer1 == "scissors":
        if computer2 == "paper":
            print("Computer1 wins")
        else:
            print("Computer2 wins")
    elif computer1 == "paper":
        if computer2 == "rock":
            print("Computer1 wins")
        else:
            print("Computer2 wins")
    else:
        print("Invalid choice")

def player_vs_player():
    print("Player vs Player")
    player1 = input("Enter your choice: ")
    player2 = input("Enter your choice: ")
    print(f"Player1 choice: {player1}")
    print(f"Player2 choice: {player2}")
    if player1 == player2:
        print("It's a tie")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player1 wins")
        else:
            print("Player2 wins")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player1 wins")
        else:
            print("Player2 wins")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player1 wins")
        else:
            print("Player2 wins")
    else:
        print("Invalid choice")

def main():
    
    player_score = 0
    computer_score = 0
    play_again = True

    

    while True:
        choice = mode()
        if choice == "1":
            player_vs_computer()
        elif choice == "2":
            computer_vs_computer()
        elif choice == "3":
            player_vs_player()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()