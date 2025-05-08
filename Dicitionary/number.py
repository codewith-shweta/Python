#number guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)


gueses = 0
is_running = True

print("PYTHON NUMBER GUESSING GAME ")
print(f"Select a number between {lowest_num} and {highest_num}: ")

while is_running:

    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        gueses  += 1

        if guess < lowest_num or guess > highest_num:
            print("The number is out of range ")

        elif guess < answer:
            print("Too low! Try again...")

        elif guess > answer:
            print("Too high! Try again...")

        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses {gueses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}: ")                                                                                                                    