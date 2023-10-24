import random
import string
from words import words
from hangman_visual import lives_visual_dict

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word and ' ' in word:
        word=random.choice(words)
    return word.upper()


def hangman():
    word=get_valid_words(words)
    word_letters=set(word) # letters in words
    alpabet=set(string.ascii_uppercase)
    used_letters=set() #letter user guessed


    lives=7
    #user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print(f"You have {lives} lives left, You have already used this letter", " ".join(used_letters))

        #word line
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word:", " ".join(word_list))
        
        user_letter=input('Guess the letter: ').upper()
        if user_letter in alpabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives=lives-1
                print("Letter is not found")

        elif user_letter in word_letters:
            print("Oops! you have alredy used this letter try once again")

        else:
            print("Invalid letter, Try once again")
    
    if lives==0:
        print(lives_visual_dict[lives])
        print("Sory, u dead. The word was",word)
    else:
        print(f"Yeah! you guessed the word {word} correctly")
            

hangman()


