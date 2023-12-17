import random

# funtion for a guessing game
def guessing_game():
    secret_number = random.randint(1,20)
    attemps = 0
    max_attemps = 5

    print("WELCOME TO ADEJOKE'S GUESSING GAME! I AM THINKING OF A NUMBER BETWEEN 1 TO 20")
    for attemps_taken in range(1, max_attemps + 1):
        guess = int(input(f"Attemp {attemps_taken}/{max_attemps}: Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try a higher number")
        elif guess > secret_number:
            print("Too high! Try a lower number")
        else:
            print(f"Congratulations! you guessed the correct number ({secret_number}) in {attemps_taken} attemps!")
            break
        attemps += 1
    if attemps == max_attemps:
        print(f"Oh no you used all {max_attemps} attemps sorry.The secret number was {secret_number}.")

# calling the guessing_game funtion
guessing_game()

