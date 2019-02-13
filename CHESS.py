from random import randint
from tkinter import Tk, Canvas


def board (w, route, path):
    w.create_rectangle (200, 50, 400, 250, width = 5)
    w.create_text (230, 80, text = "a", font = ("bold", 60))
    w.create_rectangle (400, 50, 600, 250, width = 5, fill = "red")
    w.create_text (430, 80, text = "b", font = ("bold", 60))
    w.create_rectangle (600, 50, 800, 250, width = 5)
    w.create_text (630, 80, text = "c", font = ("bold", 60))
    w.create_rectangle (200, 250, 400, 450, width = 5, fill = "red")
    w.create_text (230, 280, text = "d", font = ("bold", 60))
    w.create_rectangle (400, 250, 600, 450, width = 5)
    w.create_text (430, 280, text = "e", font = ("bold", 60))
    w.create_rectangle (600, 250, 800, 450, width = 5, fill = "red")
    w.create_text (630, 280, text = "f", font = ("bold", 60))
    w.create_rectangle (200, 450, 400, 650, width = 5)
    w.create_text (230, 480, text = "g", font = ("bold", 60))
    w.create_rectangle (400, 450, 600, 650, width = 5, fill = "red")
    w.create_text (430, 480, text = "h", font = ("bold", 60))
    w.create_rectangle (600, 450, 800, 650, width = 5)
    w.create_text (630, 480, text = "i", font = ("bold", 60))
    
    w.create_text (500, 695, text = "Route " + route, font = ("bold", 30))
    w.create_text (500, 20, text = "Path: " + path, font = ("bold", 30))


def a (w):
    w.create_rectangle (250, 150, 350, 160, width = 5, fill = "black")
def b (w):
    w.create_rectangle (450, 150, 550, 160, width = 5, fill = "black")
def c (w):
    w.create_rectangle (650, 150, 750, 160, width = 5, fill = "black")
def d (w):
    w.create_rectangle (250, 350, 350, 360, width = 5, fill = "black")
def e (w):
    w.create_rectangle (450, 350, 550, 360, width = 5, fill = "black")
def f (w):
    w.create_rectangle (650, 350, 750, 360, width = 5, fill = "black")    
def g (w):
    w.create_rectangle (250, 550, 350, 560, width = 5, fill = "black")
def h (w):
    w.create_rectangle (450, 550, 550, 560, width = 5, fill = "black")
def i (w):
    w.create_rectangle (650, 550, 750, 560, width = 5, fill = "black")  
    
def movement (routes, path):
    switch = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h, "i": i}
    
    animation = Tk ()
    w = Canvas(animation, width=1000, height=700, bg = "white")
    w.pack ()
    
    for k, route in enumerate(routes, 1):
        for square in route:
            board (w, str(k)+ ": " + route, path)
            try:
                switch [square](w)
            except:
                continue
            animation.after (1000*1, animation.update())
            w.delete ("all")
        w.delete ("all")
    animation.destroy ()

def routes(current, path):
    #diccionario de estados
    switch = {
            'a': {'W': 'e', 'R': 'bd'},
            'b': {'W': 'ace', 'R': 'df'},
            'c': {'W': 'e', 'R': 'bf'},
            'd': {'W': 'aeg', 'R': 'bh'},
            'e': {'W': 'acgi', 'R': 'bdfh'},
            'f': {'W': 'cei', 'R': 'bh'},
            'g': {'W': 'e', 'R': 'dh'},
            'h': {'W': 'egi', 'R': 'df'},
            'i': {'W': 'e', 'R': 'fh'},
            }
    #cuando el camino es vacio, regresa el mismo estado
    if not path:
        yield current
        return
    #primer caracter del camino y el resto en tupla
    first, *newpath = path
    #nuevo camino a seguir
    for state in switch[current][first]:
        #calculo de nuevo camino
        for route in routes(state, newpath):
            #regresa todo el camino en un generador
            yield current + route

def chess(path):
    global contador
    fr = open ("ROUTES_" + str(contador) + ".txt", "w")
    fw = open ("WROUTES_" + str(contador) + ".txt", "w")
    
    fr.write ("Path: " + path + "\n\n")
    for i, r in enumerate (routes('a', path), 1):
        fr.write ("Route " + str (i) + ": " + r + "\n")
        if r [len (r) - 1] == "i":
            fw.write (r + "\n")
    fr.close ()        
    fw.close ()
    

    fw = open ("WROUTES_" + str(contador) + ".txt", "r")
    nwroutes = len(fw.readlines())
    drawlines = []
    
    if nwroutes > 3:
        randline = 0
        numsrand = []

        while len (drawlines) < 3:
            randline = randint (0, nwroutes - 1)
            if randline in numsrand:
                continue
            numsrand.append (randline)
            fw = open ("WROUTES_" + str(contador) + ".txt", "r")
            for i, line in enumerate (fw):    
                if i == randline:
                    drawlines.append (line)
                    break
    elif nwroutes <= 3:
        fw = open ("WROUTES_" + str(contador) + ".txt", "r")
        for i, line in enumerate (fw):
            drawlines.append (line)
    
    fw.close ()
    
    if len(drawlines) != 0:
        movement (drawlines, path)    
    else:
        print ("No winner routes!")
        
def run ():
    global contador
    menu_opcion = 0
    while (menu_opcion != 2):
        try:
            menu_opcion = int(input ("MENU:\n\n[1] PROMPT \n[2] EXIT\n\nOPTION : "))
        except:
            menu_opcion = 0
            continue
        if menu_opcion not in range (4):
            continue
        elif menu_opcion == 1:
            chess (input ("PATH: "))
            contador += 1
            print ("\nDONE!\n")

contador = 1