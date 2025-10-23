import random

print('#### ---> Guessing game <--- ####')

guess_attempts = 0
number = random.randint(1, 10)
max_attempts = 3

print("""
Guess the correct number between 1-10 in 3 guesses.
If you don't get it right after 3 attempts you lose the game.
""")

while guess_attempts < max_attempts:
    try:
        gamer_guess = int(input("Enter your guess: "))

        if gamer_guess < 1 or gamer_guess > 10:
            print("❌ Please enter a number between 1 and 10!")
            continue

        if gamer_guess == number:
            print(f"✅ CORRECT! You guessed the number {number}!")
            break
        else:
            guess_attempts += 1
            remaining = max_attempts - guess_attempts
            if remaining > 0:
                hint = "higher" if gamer_guess < number else "lower"
                print(f"❌ Sorry, that's not correct. Try {hint}! Remaining attempts: {remaining}")
            else:
                print(f"😞 You are out of guesses. The correct number was {number}.")
    except ValueError:
        print("❌ Please enter a valid number!")
