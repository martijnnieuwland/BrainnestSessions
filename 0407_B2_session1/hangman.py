'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''
    
# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''


from random import choice


print(f"Welcome to Hangman!")

words = ['event', 'independence', 'method', 'menu', 'tongue', 'nature', 'army',
         'map', 'baseball', 'manager', 'cookie', 'appearance', 'union', 'marriage',
         'physics', 'food', 'apple', 'mall', 'analysis', 'debt', 'dirt', 'speaker',
         'presence', 'activity', 'buyer', 'drawer', 'energy', 'preference']


def again():
    if input("Want to play again? y/n: ") == "y":
        play()
    else:
        print("OK, thanks for playing! Until next time!")
        
        
def play():
    word = choice(words)
    print(word)
    letters = {}
    progress = {}
    tries = 6
    usedLetters = ""

    for letter in enumerate(word):
        letters[letter[0]] = letter[1]
        progress[letter[0]] = "_"

    while tries > 0:
        result = ""

        for letter in progress:
            result += progress[letter] + " "

        print(f"\nYou have {tries} tries left.")
        print(f"Used letters: {usedLetters}")
        print(f"Word: {result}")
        guess = input("Guess a letter: ")

        for letter in letters:
            if guess == letters[letter]:
                progress[letter] = guess

        if progress == letters:
            print(f"You guessed the word {word}!")
            again()
            break

        usedLetters += guess + " "

        if guess not in letters.values():
            tries -= 1

        if tries == 0:
            print(f"Sorry, you lost. The word was {word}!")
            again()
    
play()
