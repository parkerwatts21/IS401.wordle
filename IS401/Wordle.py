# File: Wordle.py

"""
Parker Watts, Aiki Takaku, Donna Kim, Mac Hartsell
Description : Write a python program that simulates the game wordle

I have completed Milestone 1 so far. I added comments to see where I added my code
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle(sWordOfTheDay):
    
    # Make a function to see if the user input is the same word - (Aiki) MILESTONE #2
    def enter_action(s):
        user_guess = s.upper()  # Assuming s is the input string from the user
        
        # Checks the input if it the correct word, in the word list, or not in the word list.
        if user_guess == sWordOfTheDay.upper():
            gw.show_message("Congratulations! You guessed the entire word!")
        elif user_guess.lower() in FIVE_LETTER_WORDS:
            gw.show_message("This is in the word list, but not correct.")
        else:
            gw.show_message("Not in word list.")

        # Checks each individual letter and adds color
        sCorrectLetterOne = sWordOfTheDay[0]
        sCorrectLetterTwo = sWordOfTheDay[1]
        sCorrectLetterThree = sWordOfTheDay[2]
        sCorrectLetterFour = sWordOfTheDay[3]
        sCorrectLetterFive = sWordOfTheDay[4]
        
        for iCount in range(5):
            sGuessedLetter = user_guess[iCount]
            sCorrectLetter = sWordOfTheDay[iCount]

            if (sGuessedLetter.lower() == sCorrectLetter):
                gw.set_square_color(N_ROWS - 6, iCount, CORRECT_COLOR)

            elif (sGuessedLetter.lower() in [sCorrectLetterOne, sCorrectLetterTwo, sCorrectLetterThree, sCorrectLetterFour, sCorrectLetterFive]):
                gw.set_square_color(N_ROWS - 6, iCount, PRESENT_COLOR)

            else :
                 gw.set_square_color(N_ROWS - 6, iCount, MISSING_COLOR)
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    """ (Parker) MILESTONE #1 - Putting the the word of the day using the function Set_Square_Letter and looping through each letter
      for iCount in range(5):
        sLetter = sWordOfTheDay[iCount]
        gw.set_square_letter(N_ROWS - 6, iCount, sLetter)
    """


# Selecting a random word from the dictionary and setting variables - (Parker) MILESTONE #1 
iNum = random.randrange(0, len(FIVE_LETTER_WORDS) + 1)  # Corrected range
sWordOfTheDay = FIVE_LETTER_WORDS[iNum]

# Startup code
if __name__ == "__main__":
    wordle(sWordOfTheDay)

# Testing to see what the random word is by printing - (Parker) MILESTONE #1
print(iNum)
print(sWordOfTheDay)

