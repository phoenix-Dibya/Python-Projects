import random
import string
from words import words
def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    lives = 5
    word = get_valid_word()
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters)>0 and lives>0:
        print('You  used these words ',' '.join(used_letters))
        #print the current guessed letters in word and other unguessed as --
        current_word = [letter if letter in used_letters else '-' for letter in word]
        print('Your current word is ',' '.join(current_word))
        #add the guessed letter in used_letter list and remove the correctly guessed letters from the actual word
        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabets-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                
        elif user_letter in used_letters:

            print('You have already used the letter .Please try again.')
        else:
            print('Invalid Character')
    if lives == 0:
        print('You died,The word was ',word)
    else:
        print('yay!,you won')

hangman()