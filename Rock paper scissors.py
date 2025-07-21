import random
import os
import time

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
round_number = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' anytime to quit.\n")

def get_user_choice():
    while True:
        choice = input("Your choice (rock/paper/scissors): ").strip().lower()
        if choice in choices:
            return choice
        elif choice == 'exit':
            return None
        else:
            print("Invalid input. Please type rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    global user_score, computer_score
    print(f"\n🧍 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")

    if user == computer:
        print("Result: It's a TIE!")
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You WIN this round!")
        user_score += 1
        return "user"
    else:
        print("Result: Computer WINS this round!")
        computer_score += 1
        return "computer"

def show_scores():
    print(f"\n📊 Scoreboard after Round {round_number}:")
    print(f"🧍 You: {user_score}")
    print(f"🤖 Computer: {computer_score}")

def ask_play_again():
    choice = input("\nPlay another round? (y/n): ").strip().lower()
    return choice == 'y'

def main():
    global round_number
    clear_screen()
    print_welcome()

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        if user_choice is None:
            break

        computer_choice = get_computer_choice()
        decide_winner(user_choice, computer_choice)
        show_scores()

        if not ask_play_again():
            break

        round_number += 1
        time.sleep(1)
        clear_screen()

    print("\nThanks for playing! Final Scores:")
    show_scores()
    print("Goodbye 👋")

if __name__ == "__main__":
    main()
