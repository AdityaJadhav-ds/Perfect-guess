import random

def number_guessing_game():
    
    target = random.randint(1, 100)
    attempts = 0
    guess = None

    print("\n🎮 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?\n")

    while guess != target:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess == target:
                print(f"\n✅ Congratulations! You guessed the correct number: {target}")
                print(f"📊 You took {attempts} attempt(s).")
                print("🎉 Now let your friend try!\n")
                break
            elif guess < target:
                print("🔼 Try a higher number!\n")
            else:  # guess > target
                print("🔽 Try a lower number!\n")

        except ValueError:
            print("⚠️ Please enter a valid integer.\n")

if __name__ == "__main__":
    number_guessing_game()

