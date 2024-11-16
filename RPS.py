import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please choose again (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == 'rock':
        if computer_choice == 'scissors':
            return "You win! Rock beats Scissors."
        else:
            return "You lose! Paper beats Rock."
    if user_choice == 'paper':
        if computer_choice == 'rock':
            return "You win! Paper beats Rock."
        else:
            return "You lose! Scissors beat Paper."
    if user_choice == 'scissors':
        if computer_choice == 'paper':
            return "You win! Scissors beat Paper."
        else:
            return "You lose! Rock beats Scissors."

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    result = determine_winner(user_choice, computer_choice)
    print(result)
if __name__ == "__main__":
    play_game()