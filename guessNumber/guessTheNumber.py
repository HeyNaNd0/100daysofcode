print('#### ---> Guessing game <--- ####') 

guess_attempts = 0
number = 6
max_attempts = 3

print("""
Guess the correct number between 1-10 in 3 guesses.
If you don’t get it right after 3 attempts you lose the game.
""")

while guess_attempts < max_attempts:
    gamer_guess = int(input("Enter your guess: "))
    
    if gamer_guess == number:
        print(f"✅ CORRECT! You guessed the number {number}!")
        break
    else:
        guess_attempts += 1
        remaining = max_attempts - guess_attempts
        if remaining > 0:
            print(f"❌ Sorry, that’s not correct. Remaining attempts: {remaining}")
        else:
            print(f"😞 You are out of guesses. The correct number was {number}.")
