import random


def guess(x):
    random_integer = random.randint(1, x)
    guess = 0
    while(guess != random_integer):
        guess = int(input(f"Guess a random number between 1 to {x}: "))
        if(guess < random_integer):
            print("Too Low. Guess Again")
        elif(guess > random_integer):
            print("Too High. Guess Again")    

    print(f"Congratulation you have guessed right number i.e. {guess}.")

guess(50)