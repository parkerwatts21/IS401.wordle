# Parker Watts, Aiki Takaku, Donna Kim, Mac Hartsell
# Description : Write a python program 
# Overall GPA, Last 30 Credits GPA, Accounting 200 Grade, IS 201 Grade, IS 303 Grade, Essay score between 0 and 4 
# Convert these variables into correct values, calculate Total Applying GPA, and then display Total Applying GPA with correlating message

# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle(sWordOfTheDay):

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    for iCount in range (0, 5, 1) :
        sLetter = sWordOfTheDay[iCount]
        gw.get_square_letter(1, iCount, sLetter)

# Startup code
iNum = random.randrange(0, len(FIVE_LETTER_WORDS) + 1)
sWordOfTheDay = FIVE_LETTER_WORDS[iNum]

if __name__ == "__main__":
    wordle(sWordOfTheDay)

print(iNum)
print(sWordOfTheDay)
