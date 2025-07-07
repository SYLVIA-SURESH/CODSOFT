import random
import string

def get_complexity_choice():
    print("\nChoose password complexity level:")
    print("1. Letters only (Simple)")
    print("2. Letters and Digits (Moderate)")
    print("3. Letters, Digits, and Symbols (Complex)")
    return input("Enter your choice (1/2/3): ")

def generate_password(length, choice):
    if choice == '1':
        characters = string.ascii_letters
    elif choice == '2':
        characters = string.ascii_letters + string.digits
    elif choice == '3':
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
    else:
        return None
    return ''.join(random.choice(characters) for _ in range(length))

def get_password_strength(length, choice):
    if length < 6:
        return "Weak"
    elif choice == '1':
        return "Weak"
    elif choice == '2':
        return "Medium"
    elif choice == '3' and length >= 8:
        return "Strong"
    return "Medium"

def main():
    print("\n🔐 SIMPLE & SMART PASSWORD GENERATOR 🔐")
    try:
        length = int(input("Enter desired password length (4–16 recommended): "))
        if length < 4 or length > 32:
            print("❌ Please choose a length between 4 and 32.")
            return

        choice = get_complexity_choice()
        password = generate_password(length, choice)

        if not password:
            print("❌ Invalid choice.")
            return

        strength = get_password_strength(length, choice)

        print(f"\n🔑 Generated Password: {password}")
        print(f"🔒 Password Strength: {strength}")

        save = input("💾 Save password to file? (y/n): ").lower()
        if save == 'y':
            with open("passwords.txt", "a") as f:
                f.write(f"{password} | Strength: {strength}\n")
            print("✅ Saved to 'passwords.txt'.")

    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
