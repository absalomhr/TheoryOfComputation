# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:28:03 2017

@author: abzar
"""
from STACK import Stack
from tkinter import Tk, Canvas
import time


def circle(canvas, x, y, r, width):
    canvas.create_oval (x-r, y-r, x+r, y+r, width = width)
def line_circle (canvas, x1, y1, x2, y2, width):
    canvas.create_line (x1, y1, x2, y2, width = width)
    circle (canvas, x2, y2, 3, 8)

def board (state, string, stack, canvas):
    line_circle (canvas, 500, 250, 500, 100, 3)
    canvas.create_text (500, 70, text = string, font = ("bold", 30))
    line_circle (canvas, 500, 450, 500, 600, 3)
    canvas.create_text (500, 630, text = stack, font = ("bold", 30))
    canvas.create_rectangle (400, 250, 600, 450, fill = "blue")
    canvas.create_text (500, 350, text = state, font = ("bold", 60))
    canvas.after (1000*1, canvas.update())
    canvas.delete ("all")

def pda (f, string):

    s = Stack ()
    animation = Tk ()
    w = Canvas(animation, width=1000, height=700, bg = "white")
    w.pack ()
    
    s.push ("Z")
    state = "q"
    seen1 = False
    i = 0
    
    
    
    while string [i] == "0":   
        if state == "q" and s.top () == "X" and string [i] == "0":
            f.write ("(" + state + ", " + string [i:len (string) - 1:] + ", " + s.showStack () + ")" + "|-")
            board (state, string [i:len (string) - 1:], s.showStack (), w)
            s.push ("X")
        elif state == "q" and s.top () == "Z" and string [i] == "0":
            f.write ("(" + state + ", " + string [i:len (string) - 1:] + ", " + s.showStack () + ")" + "|-")
            board (state, string [i:len (string) - 1:], s.showStack (), w)
            s.push ("X")
        i += 1
    while string [i] == "1":
        seen1 = True
        if s.top () == "Z":
            break
    
        if state == "p" and s.top () == "X" and string [i] == "1":
            f.write ("(" + state + ", " + string [i:len (string) - 1:] + ", " + s.showStack () + ")" + "|-")
            board (state, string [i:len (string) - 1:], s.showStack (), w)
            s.pop ()
        elif state == "q" and s.top () == "X" and string [i] == "1":
            f.write ("(" + state + ", " + string [i:len (string) - 1:] + ", " + s.showStack () + ")" + "|-")
            board (state, string [i:len (string) - 1:], s.showStack (), w)
            state = "p"
            s.pop ()
        i += 1


    if state == "p" and string [i::] == "e" and s.top () == "Z":
        #happy road
        f.write ("(" + state + ", " + string [i::] + ", " + s.showStack () + ")" + "|-")
        board (state, string [i::], s.showStack (), w)
        state = "f"
        f.write ("(" + state + ", " + string [i::] + ", " + s.showStack () + ")")
        board (state, string [i::], s.showStack (), w)
        f.write ("\n\nSTRING BELONGS TO L")
    elif state == "p" and string [i::] == "e" and s.top () == "X":
        f.write ("(" + state + ", " + string [i::] + ", " + s.showStack () + ")" + "|-")
        state = "f"
        f.write ("(" + state + ", " + string [i::] + ", " + s.showStack () + ")")
        f.write ("\n\nSTRING DOESN'T BELONG TO L")
    else:
        #caso de solo 1s o 01 y luego 0
        if seen1 == True:
            f.write ("(" + state + ", " + string [i:len (string) - 1:] + ", " + s.showStack () + ")" )
            board (state, string [i:len (string) - 1:], s.showStack (), w)
            if state == "p" and string [i] == "0" and s.showStack () == "Z":
                state = "f"
                f.write ("|-")
                f.write ("(" + state + ", " + string [i:len (string) - 1:] + ", " + s.showStack () + ")")
                board (state, string [i:len (string) - 1:], s.showStack (), w)
            elif state == "p" and string [i] == "1" and s.showStack () == "Z":
                state = "f"
                f.write ("|-")
                f.write ("(" + state + ", " + string [i:len (string) - 1:] + ", " + s.showStack () + ")")
                board (state, string [i:len (string) - 1:], s.showStack (), w)
            elif state == "p" and string [i] == "e" and s.top () == "X":
                f.write ("|-")
                f.write ("(" + state + ", " + string [i::] + ", " + s.showStack () + ")")
                board (state, string [i::], s.showStack (), w)
            
        #caso de solo 0s
        elif seen1 == False:
            f.write ("|-")
            f.write ("(" + state + ", " + string [i::] + ", " + s.showStack () + ")")
            board (state, string [i::], s.showStack (), w)
        f.write ("\n\nSTRING DOESN'T BELONG TO L")

    time.sleep (1)
    animation.destroy ()
    
def run ():
    global contador
    menu_opcion = 0
    while (menu_opcion != 3):
        try:
            menu_opcion = int(input ("MENU:\n\n[1] PROMPT\n[2] FILE\n[3] EXIT\n\nOPTION : "))
        except:
            menu_opcion = 0
            continue
        if menu_opcion not in range (4):
            continue
        elif menu_opcion == 1:
            f = open ("PDA_PROMPT_" + str (contador) + ".txt", "w")
            pda (f, input ("STRING: ") + "e")
            f.close ()
            contador += 1
            print ("\nDONE!\n")
        elif menu_opcion == 2:
            workfile =  input ("FILE NAME: ")
            try:
                fr = open (workfile + ".txt", 'r')
                f = open ("PDA_FILE_" + str (contador) + ".txt", "w")
                pda (f, fr.read() + "e")
                fr.close()
                f.close ()
                contador += 1
                print ("\nDONE!\n")
            except:
                print ("\nFILE NOT FOUND\n")        
contador = 1