import random

def get_user_choice():
    print("\n👊 Welcome to Rock-Paper-Scissors Game!")
    print("Choose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (1/2/3): ")
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    return choices.get(choice, None)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You Win! 🎉"
    else:
        return "You Lose! 😢"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if not user_choice:
            print("❌ Invalid input. Please select 1, 2, or 3.")
            continue

        computer_choice = get_computer_choice()
        print(f"\n🧍 You chose: {user_choice.capitalize()}")
        print(f"💻 Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\n🏁 Result: {result}")

        # Update scores
        if "Win" in result:
            user_score += 1
        elif "Lose" in result:
            computer_score += 1

        print(f"\n📊 Scores => You: {user_score} | Computer: {computer_score}")

        play_again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\n🎮 Thanks for playing Rock-Paper-Scissors!")
            break

if __name__ == "__main__":
    main()
