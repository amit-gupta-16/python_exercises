# Number guessing program(game)
n = 20
attempts = 5
print("This a simple number Guessing Game!\n Guess the correct number and win!")
print("\n Plz enter number between 1 to 50")
print("Total attempts = 5")
while True:
    inp = int(input("\nEnter your number:"))
    if inp < n:
        print("Try a greater number!\n", end="")
        attempts = attempts - 1
        if attempts == 0:
            print("You Lose!")
            break
        print("Attempts left:", attempts)
    elif inp > n:
        print("Try a smaller number!\n", end="")
        attempts = attempts - 1
        if attempts == 0:
            print("You Lose!")
            break
        print("Attempts left:", attempts)
    elif inp == n:
        print("\nYou won!")
        print("Attempts to finish the game: ", 6 - attempts)
        break
# Amit Gupta makes this program!

