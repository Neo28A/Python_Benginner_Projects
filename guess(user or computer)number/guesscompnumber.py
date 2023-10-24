
import random

def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess the number between 1 to {x}: "))

        if guess > random_number:
            print("Oops! you guessed to high")
        elif guess< random_number:
            print("Oops! you guessed to low")

    print(f"Yeah! congrats you have guessed the number {random_number} correctly ")


guess(20)
