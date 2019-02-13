# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:02:35 2017

@author: abzar
"""

import WEBAY
import REGEX
import CHESS
import PALINDROME
import PDA

contador = 0
menu = 0

while menu != 6:
    try:
        menu = int(input ("MENU:\n\n[1] WEBAY\n[2] REGEX\n[3] CHESS\n[4] PALINDROME\n[5] PDA\n[6] EXIT\n\nOPTION: "))
    except:
        menu = 0
        continue
    if menu not in range (6):
        continue
    elif menu == 1:
        WEBAY.run ()
    elif menu == 2:
        REGEX.run ()
    elif menu == 3:
        CHESS.run ()
    elif menu == 4:
        PALINDROME.run ()
    elif menu == 5:
        PDA.run ()