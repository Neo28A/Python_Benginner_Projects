import random

def computer_guess(x):
    low=1
    high=x

    feedback=" "
    while feedback != "c":
        if low != high:
            guess=random.randint(low,high)
        else:
            guess=low

        feedback=input(f"Is number {guess} is too high (h) or too low (l) or correct (c) ?".lower())

        if feedback== "h":
            high=guess-1
        elif feedback=="l":
            low = guess+1
    
    print(f"wow! you have guessed the number {guess} correctly")

computer_guess(500)
