import random
random_number = random.randint(1, 20)

guess = 0
while guess != random_number:
    guess = int(input("Guess the number (between 1 and 20): "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
