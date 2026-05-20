# Build a Number Guessing Game: 5 attempts,
# hints given (too high/low).

import random

secret_number = random.randint(1,100)
print(secret_number)

is_running = True
attempts = 0
guess_list = []

while is_running:
    guess = int(input("Enter Your Guess. It is between 1 and 100!: "))

    if guess < 1 or guess > 100:
        print("The range is between 1-100! Try Again: ")
        continue

    
    attempts +=1
    guess_list.append(guess)

    if guess == secret_number:
        print("CONGRATULATIONS!! YOU GUESSED THE NUMBER RIGHT!")
        print("Game Over")
        print(guess_list)
        break

    elif attempts >= 5:
        print("You have no attempts left!!")
        print("Game Over")
        print(f"The secret number was {secret_number}")
        break

    elif guess < secret_number:
        print("Take a Higher Guess!! : ")

    elif guess > secret_number:
        print("Take a lower guess! : ")
    
print(guess_list)

