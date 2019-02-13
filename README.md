# This programs were implemented as excersises in the class Computational Theory.

To execute them you can run GENERAL.py, from there everything is on a menu.
The results of all the computations made by the programms are stored in files.
These programs were suggested by Dr. Genaro Juarez Martínez.

Here I give a brief explanation of what each programm does:

## 1. WEBAY.py
This program reads a text (file or manually typed) and finds the strings "web" and "ebay".
It also finds the position where they were found. All of of this through a deterministic
automaton. It can also show a visualization of the automaton made with Tkinter:

![GitHub Logo](/Test/CapturaGraphWEBAY.PNG)

## 2. REGEX.py
This program has preloaded two regular expressions from which it will generate 5 strings.
Here's the code for the first one as an example:

``` python

def regex1 ():
    #partes de la cadena
    parte1 = ""
    parte2 = ""
    
    #calculo de parte 1: (0 + 10)*
    #0, 10 o epsilon
    #1 = 0, 2 = 10
    flag = randint (1, 2)
    if flag == 1:
        parte1 = "0"
    elif flag == 2:
        parte1 = "10"
    #universo, en el 0 esta epsilon
    flag = randint (0, 1000)
    parte1 = parte1*flag
    
    #calculo de parte 2: (e +1)
    #epsilon o 1
    flag = randint (1, 2)
    if flag == 1:
        parte2 = ""
    elif flag == 2:
        parte2 = "1"
    
    #cadena generada
    return parte1 + parte2

```

## 3. CHESS.py
This program calculates all the possible routes on a 3x3 chessboard starting in the first
square to the last (a -> i). It receives a string of colors of the squares (W = white,
R = red) and finds all the routes that match those colors, then if there is at least one
route that goes from square a to square i, it will show the animation of the route.

Try it with the following input for a better understandig of the programm:
"WW"

Here's the output:

![GitHub Logo](/Test/CapturaBoardCHESS.PNG)

All the results are stored in files for further reading (All routes and "winning routes",
meaning routes that go from square a to square i.

## 4. PALINDROME.py
This program generates a binary palindrome of random or user-given lenght following
certain production rules.

Generating a palindrome of size 20 gives the next output:

![GitHub Logo](/Test/CapturaPALINDROME.PNG)

## 5. PDA
This programm is a pushdown automaton. It will determine whether the input string has "n" 0's
followed by "n" 1's. It produces the animation of the automaton storing and retrieving
values from the stack.

![GitHub Logo](/Test/CapturaPDA.PNG)

If you have any questions feel free to contact me.
