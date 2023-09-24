import random

# This is a comment
#
# It doesn't do anything special, just allows you to leave notes 
# for yourself and others

# Create a list of scores with the values 1.0, 5.0, 6.0, and 2.0
# Average them and print the result

magic = random.randint(1, 10)

print("This is a guessing game")
attempts = int(input("How many attempts would you like? "))

did_win = False
for attempt in range(1, attempts + 1):
    print("Attempt number", attempt)
    guess = int(input("What is your guess? "))

    if guess == magic:
        did_win = True
        break
    elif guess > magic:
        print("Too high!")
    elif guess < magic:
        print("Too low!")

if did_win:
    print("You win :)")
else:
    print("You lose :(")