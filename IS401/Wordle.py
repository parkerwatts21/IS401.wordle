# File: Wordle.py

"""
Parker Watts, Aiki Takaku, Donna Kim, Mac Hartsell
Description : Write a python program that simulates the game wordle

I have completed Milestone 1 so far. I added comments to see where I added my code
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle(sWordOfTheDay):
    
    # Make a function to see if the user input is the same word - (Aiki) MILESTONE #2
    def enter_action(s):
        user_guess = s.upper()  # Assuming s is the input string from the user
        
        if user_guess == sWordOfTheDay.upper():
            gw.show_message("Congratulations! You guessed the entire word!")
        else:
            gw.show_message("Not the correct word.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Putting the the word of the day using the function Set_Square_Letter and looping through each letter - (Parker) MILESTONE #1
    for iCount in range(5):
        sLetter = sWordOfTheDay[iCount]
        gw.set_square_letter(N_ROWS - 6, iCount, sLetter)


# Selecting a random word from the dictionary and setting variables - (Parker) MILESTONE #1 
iNum = random.randrange(0, len(FIVE_LETTER_WORDS) + 1)  # Corrected range
sWordOfTheDay = FIVE_LETTER_WORDS[iNum]

# Startup code
if __name__ == "__main__":
    wordle(sWordOfTheDay)

# Testing to see what the random word is by printing - (Parker) MILESTONE #1
print(iNum)
print(sWordOfTheDay)

