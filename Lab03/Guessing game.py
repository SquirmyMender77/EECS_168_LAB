print("Welcome to the Guessing Game")
import random
while True:
    number=random.randint(-100,100)
    guess_count=0
    closest_guess= None
    while True:
        guess=int(input("Guess a number (-100 - 100): "))
        guess_count += 1
        if guess == number:
            print("congrats, you got it!")
            break
        elif guess<number:
            print("Too low!")
        elif guess>number:
            print("Too high!")
    print(f" It took you {guess_count} guesses!")
    again = input("Play again? (y/n): ").lower()
    if again == 'n':
        print("Goodbye!")
        break
