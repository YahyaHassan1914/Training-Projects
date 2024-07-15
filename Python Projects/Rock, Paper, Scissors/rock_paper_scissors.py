import random

class QuitGameException(Exception):
    pass

def get_input(prompt, quit_keyword='q'):
    user_input = input(prompt).strip().lower()
    if user_input == quit_keyword:
        raise QuitGameException
    return user_input

def quit_game():
    print("Quitting the game. Goodbye!")
    exit()

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    choice = get_input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in choices:
        print("Invalid choice. Please try again.")
        choice = get_input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def main():
    print("Welcome to the Advanced Rock, Paper, Scissors Game!")
    print("You can play multiple rounds and keep track of the score.")
    print("You can press 'q' to quit the game.")

    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        try:
            rounds += 1
            print(f"\nRound {rounds}")

            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            winner = determine_winner(user_choice, computer_choice)
            if winner == 'tie':
                print("It's a tie!")
            elif winner == 'user':
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

            print(f"Score -> You: {user_score}, Computer: {computer_score}")

            play_again = get_input("Do you want to play another round? (yes/no): ").lower()
            if play_again != 'yes':
                break

        except QuitGameException:
            quit_game()

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()