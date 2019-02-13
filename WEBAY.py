# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:11:52 2017

@author: abzar
"""
from tkinter import Tk, Canvas, mainloop
#funciones para graficar elementos del automata
def circle(canvas, x, y, r, width):
   id = canvas.create_oval (x-r, y-r, x+r, y+r, width = width)
   return id
def line (canvas, x1, y1, x2, y2, width):
    canvas.create_line (x1, y1, x2, y2, width = width)
def line_circle (canvas, x1, y1, x2, y2, width):
    canvas.create_line (x1, y1, x2, y2, width = width)
    circle (canvas, x2, y2, 3, 8)    
def text (canvas, x, y, text):
    canvas.create_text (x, y, text = text, font = ("bold", 15))
def loop (canvas, x, y, lado, texto):
    r = 20
    h = 30
    
    if lado == "ab":
        circle (canvas, x, y - r, r, 3)
        circle (canvas, x, y, 3, 8)
        canvas.create_text (x, y - r - h, text = texto, font = ("bold", 15))
    elif lado == "ar":
        circle (canvas, x, y + r, r, 3)
        circle (canvas, x, y, 3, 8)
        canvas.create_text (x, y + r + h, text = texto, font = ("bold", 15))
    elif lado == "izq":
        circle (canvas, x + r, y, r, 3)
        circle (canvas, x, y, 3, 8)
        canvas.create_text (x  + r, y - r - h, text = texto, font = ("bold", 15))
    elif lado == "der":
        circle (canvas, x - r, y, r, 3)
        circle (canvas, x, y, 3, 8)
        canvas.create_text (x  - 2 * r - h - 10, y, text = texto, font = ("bold", 15))
    
def draw_auto ():
    #se crea el Canvas
    w = Canvas(Tk (), width=1000, height=600, bg = "white")
    
    #coordenadas estado inicial
    x = 180
    y = 270
    #distancia entre estados horizontal
    s = 0.85
    #distancia entre estados vertical
    t = 1
    #radio circulo
    r = 40
    #ancho del circulo y linea
    a = 3
    #altura de las letras respecto a las lineas horizontales
    h = 15
                
    #circulo de inicio
    circle (w , x, y, r, a)
    text (w, x, y, "1")
    
    #circulos de arriba en orden ascendente (web)
    circle (w , x + 200 * s, y - 100 * t, r, a)
    text (w, x + 200 * s, y - 100 * t, "2")
    circle (w , x + 400 * s, y - 100 * t, r, a)
    text (w, x + 400 * s, y - 100 * t, "3")
    circle (w , x + 600 * s, y - 100 * t, r, a)
    circle (w , x + 600 * s, y - 100 * t, r - 15, a)
    text (w, x + 600 * s, y - 100 * t, "4")
    
    #circulos de abajo en orden ascendente (ebay)
    circle (w , x + 200 * s, y + 100 * t, r, a)
    text (w, x + 200 * s, y + 100 * t, "5")
    circle (w , x + 400 * s, y + 100 * t, r, a)
    text (w, x + 400 * s, y + 100 * t, "6")
    circle (w , x + 600 * s, y + 100 * t, r, a)
    text (w, x + 600 * s, y + 100 * t, "7")
    circle (w , x + 800 * s, y + 100 * t, r, a)
    circle (w , x + 800 * s, y + 100 * t, r - 15, a)
    text (w, x + 800 * s, y + 100 * t, "8")
    
    #lineas
    #linea estado 1 a estado 2 por w
    line_circle (w, x + r, y, x + 200 * s - r, y - 100 * t, a)
    text (w, (((x + 200 * s - r) - (x + r))/2) + (x + r), ((y - (y - 100 * t))/2) + (y - 100 * t) + h, "w")
    #linea estado 1 a estado 5 por e
    line_circle (w, x + r, y, x + 200 * s - r, y + 100 * t, a)
    text (w, (((x + 200 * s - r) - (x + r))/2) + (x + r), ((y - (y + 100 * t))/2) + (y + 100 * t) - h, "e")
    
    #lineas de arriba horizontales
    #linea de estado 2 a estado 3 por e
    line_circle (w, x + 200 * s + r, y - 100 * t, x + 400 * s - r, y - 100 * t, a)
    text (w, (((x + 400 * s - r) - (x + 200 * s + r))/2) + (x + 200 * s + r), y - 100 * t + h, "e")
    #lineas de estado 3 a estado 4 por b
    line_circle (w, x + 400 * s + r, y - 100 * t, x + 600 * s - r, y - 100 * t, a)
    text (w, (((x + 600 * s - r) - (x + 400 * s + r))/2) + (x + 400 * s + r), y - 100 * t + h, "b")
    
    #lineas de abajo horizontales
    #linea de estado 5 a estado 6 por b
    line_circle (w, x + 200 * s + r, y + 100 * t, x + 400 * s - r, y + 100 * t, a)
    text (w, (((x + 400 * s - r) - (x + 200 * s + r))/2) + (x + 200 * s + r), y + 100 * t - h, "b")
    #lineas de estado 6 a estado 7 por b
    line_circle (w, x + 400 * s + r, y + 100 * t, x + 600 * s - r, y + 100 * t, a)
    text (w, (((x + 600 * s - r) - (x + 400 * s + r))/2) + (x + 400 * s + r), y + 100 * t - h, "a")
    #lineas de estado 7 a estado 8 por b
    line_circle (w, x + 600 * s + r, y + 100 * t, x + 800 * s - r, y + 100 * t, a)
    text (w, (((x + 800 * s - r) - (x + 600 * s + r))/2) + (x + 600 * s + r), y + 100 * t - h, "y")
    
    #loops
    #loop sobre estado 1
    loop (w, x - r, y, "der", "S - w - e")
    #loop sobre estado 2
    loop (w, x + 200 * s, y - 100 * t - r, "ab", "w")
    #loop sobre estado 5
    loop (w, x + 200 * s, y + 100 * t + r, "ar", "e")
    
    
    #lineas de adentro verticales
    #hacia arriba
    line (w, x + 400 * s, y + 100 * t - r, x + 400 * s, y + 100 * t - r - 20, a)
    line (w, x + 600 * s, y + 100 * t - r, x + 600 * s, y + 100 * t - r - 20, a)
    line (w, x + 800 * s, y + 100 * t - r, x + 800 * s, y + 100 * t - r - 20, a)
    #linea que une
    line (w, x + 200 * s, y + 100 * t - r - 20, x + 800 * s, y + 100 * t - r - 20, a )
    #linea que va hacia estado 2 por w
    line_circle (w, x + 200 * s, y + 100 * t - r, x + 200 * s, y - 100 * t + r, a)
    text (w, x + 200 * s - h, (((y + 100 * t - r ) - (y - 100 * t + r)) / 2) + y - 100 * t + r, "w")
    
    #hacia abajo
    line (w, x + 400 * s, y - 100 * t + r, x + 400 * s, y - 100 * t + r + 20, a)
    line (w, x + 600 * s, y - 100 * t + r, x + 600 * s, y - 100 * t + r + 20, a)
    #linea que une
    line (w, x + 400 * s, y - 100 * t + r + 20, x + 600 * s, y - 100 * t + r + 20, a )
    #linea que va hacia estado 5 por e
    line_circle (w, x + 400 * s, y - 100 * t + r + 20, x + 200 * s + (r / 2) + (r / 5), y + 100 * t - (r / 2) - (r / 5), a)
    text (w, (((x + 400 * s) - (x + 200 * s))/2) + (x + 200 * s), (((y + 100 * t - (r / 2) - (r / 5)) - (y - 100 * t + r + 20))/2) + (y - 100 * t + r + 20) - h, "e")
    
    #lineas de afuera verticales
    #hacia abajo
    line (w, x + 400 * s, y + 100 * t + r, x + 400 * s, y + 100 * t + r + 20, a)
    line (w, x + 600 * s, y + 100 * t + r, x + 600 * s, y + 100 * t + r + 20, a)
    line (w, x + 800 * s, y + 100 * t + r, x + 800 * s, y + 100 * t + r + 20, a)
    #linea que une
    line (w, x + 400 * s, y + 100 * t + r + 20, x + 800 * s, y + 100 * t + r + 20, a)
    #linea que va a estado 5 de afuera por e
    line_circle (w, x + 400 * s, y + 100 * t + r + 20, x + 200 * s + (r / 2) + (r / 5), y + 100 * t + (r /2) + (r / 5), a )
    text (w, (((x + 400 * s) - (x + 200 * s))/2) + (x + 200 * s), (((y + 100 * t + r + 20) - (y + 100 * t + (r / 2)+ (r / 5)))/2) + (y + 100 * t + (r / 2) + (r / 5)) + h, "e")
    #segundas lineas hacia abajo
    line (w, x + 400 * s, y + 100 * t + r + 20, x + 400 * s, y + 100 * t + r + 100, a)
    text (w, x + 400 * s + 4 * h, y + 100 *  t + r + 100 - h, "S - a - e - w")
    line (w, x + 600 * s, y + 100 * t + r + 20, x + 600 * s, y + 100 * t + r + 100, a)
    text (w, x + 600 * s + 4 * h, y + 100 *  t + r + 100 - h, "S - e - w - y")
    line (w, x + 800 * s, y + 100 * t + r + 20, x + 800 * s, y + 100 * t + r + 100, a)
    text (w, x + 800 * s + 4 * h, y + 100 *  t + r + 100 - h, "S - e - w")
    line (w, x, y + 100 * t + r + 100, x + 200 * s - (r / 2) - (r / 5), y + 100 * t + (r / 2) + (r /5), a)
    text (w, x + 6 * h, y + 100 *  t + r + 100 - h, "S - b - e - w")
    #linea que une
    line (w, x, y + 100 * t + r + 100, x + 800 * s, y + 100 * t + r + 100, a)
    #linea que va de estados 6, 7, 8 a estado 1
    line_circle (w, x, y + 100 * t + r + 100, x, y + r, a)
    
    #hacia arriba
    line (w, x + 400 * s, y - 100 * t - r, x + 400 * s, y - 100 * t - r - 20, a)
    line (w, x + 600 * s, y - 100 * t - r, x + 600 * s, y - 100 * t - r - 20, a)
    #linea que une
    line (w, x + 400 * s, y - 100 * t - r - 20, x + 600 * s, y - 100 * t - r - 20, a)
    #linea que va a estado 2
    line_circle (w, x + 400 * s, y - 100 * t - r - 20, x + 200 * s + (r / 2) + (r / 5), y - 100 * t - (r /2) - (r / 5), a )
    text (w, (((x + 400 * s) - (x + 200 * s))/2) + (x + 200 * s), (((y - 100 * t - r - 20) - (y - 100 * t - (r / 2) - (r / 5)))/2) + (y - 100 * t - (r / 2) - (r / 5)) + h, "w")
    #segundas lienas hacia arriba
    line (w, x + 400 * s, y - 100 * t - r - 20, x + 400 * s, y - 100 * t - r - 100, a)
    text (w, x + 400 * s + 4 * h, y - 100 *  t - r - 100 + h, "S - b - e - w")
    line (w, x + 600 * s, y - 100 * t - r - 20, x + 600 * s, y - 100 * t - r - 100, a)
    text (w, x + 600 * s + 4 * h, y - 100 *  t - r - 100 + h, "S - a - e - w")
    line (w, x, y - 100 * t - r - 100, x + 200 * s - (r / 2) - (r / 5), y - 100 * t - (r / 2) - (r /5), a)
    text (w, x + 6 * h, y - 100 *  t - r - 100 + h, "S - e - w")
    #liena que une
    line (w, x, y - 100 * t - r - 100, x + 600 * s, y - 100 * t - r - 100, a)
    #linea que va de estados 2, 3 y 4 a estado 1
    line_circle (w, x, y - 100 * t - r - 100, x, y - r, a)    
    w.pack()
    mainloop()



#funciones de los estados del automata
def q1 (char, eos, f):
    global estado
    f.write ("\nEstado: q1\n")
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char != 'e' and char != 'w':
            estado = "q1"
        elif char == 'e':
            estado = "q5"
        elif char == 'w':
            estado = "q2"
            
def q2 (char, eos, f):
    global estado
    f.write ("\nEstado: q2\n")
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char == 'e':
            estado = "q3"
        elif char == 'w':
            estado = "q2"
        elif char != 'e' and char != 'w':
            estado = "q1"
            
def q3 (char, eos, f):
    global estado
    f.write ("\nEstado: q3\n")
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char == 'w':
            estado = "q2"
        elif char == 'e':
            estado = "q5"
        elif char == 'b':
            estado = "q4"
        elif char != 'w' and char != 'b' and char != 'e':
            estado = "q1"
            
def q4 (char, eos, f):
    global estado
    global cont_web
    f.write ("\nEstado: q4\n")
    cont_web += 1
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char == 'e':
            estado = "q5"
        elif char == 'a':
            estado = "q7"
        elif char == 'w':
            estado = "q2"
        elif char != 'a' and char != 'w' and char != 'e':
            estado = "q1"
            
def q5 (char, eos, f):
    global estado
    f.write ("\nEstado: q5\n")
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char == 'w':
            estado = "q2"
        elif char == 'e':
            estado = "q5"
        elif char == 'b':
            estado = "q6"
        elif char != 'b' and char != 'e' and char != 'w':
            estado = "q1"
            
def q6 (char, eos, f):
    global estado
    f.write ("\nEstado: q6\n")
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char == 'w':
            estado = "q2"
        elif char == 'e':
            estado = "q5"
        elif char == 'a':
            estado = "q7"
        elif char != 'a' and char != 'e' and char != 'w':
            estado = "q1"
            
def q7 (char, eos, f):
    global estado
    f.write ("\nEstado: q7\n")
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char == 'e':
            estado = "q5"
        elif char == 'w':
            estado = "q2"
        elif char == 'y':
            estado = "q8"
        elif char != 'e' and char != 'w' and char != 'y':
            estado = "q7"
            
def q8 (char, eos, f):
    global estado
    global cont_ebay
    cont_ebay += 1
    f.write ("\nEstado: q8\n")
    if eos == False:
        f.write ("Se lee un "+ char + "\n")
        if char == 'w':
            estado = "q2"
        elif char == 'e':
            estado = "q5"
        elif char != 'e' and char != 'w':
            estado = "q1"
            
#lectura de cadena
def automaton (f, string):    
    print ("\n")
    #estado inicial del automata
    global estado
    string = string.lower ()
    #La cadena vacia tiene paridad
    if string == "":
        f.write ("\nEstado: " + estado + "Cadena vacia")
        return
    f.write ("Comienzo:\n")
    #bandera de fin de lectura (end of string)
    eos = False
    #diccionario que se usa como switch
    switch = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6, "q7": q7, "q8": q8}
    #leer cadena
    contchar = -1
    for i in string:
        contchar = contchar + 1
        if estado == "q8":
            f.write ("Palabra \"ebay\" encontrada en "+ str(contchar) +"\n")
        elif estado == "q4":
            f.write ("Palabra \"web\" encontrada en "+ str(contchar) +"\n")
        #entrada al estado correspondiente
        switch [estado](i, eos, f)  
        f.write ("\n")
    eos = True
    switch [estado](i, eos, f)
    if estado == "q8":
            f.write ("Palabra \"ebay\" encontrada en "+ str(contchar + 1) +"\n")
    elif estado == "q4":
        f.write ("Palabra \"web\" encontrada en "+ str(contchar + 1) +"\n")
    f.write ("\nEncontradas " + str (cont_ebay) + " palabras \"ebay\"\n")
    f.write ("\nEncontradas " + str (cont_web) + " palabras \"web\"\n")
    f.close()
    estado = "q1"



#menu
def run ():
    global contador
    menu_opcion = 0
    while (menu_opcion != 4):
        try:
            menu_opcion = int(input ("MENU:\n\n[1] PROMPT\n[2] FILE\n[3] GRAPH\n[4] EXIT\n\nOPTION : "))
        except:
            menu_opcion = 0
            continue
        if menu_opcion not in range (5):
            continue
        elif menu_opcion == 1:
            f = open ("WEBAY_PROMPT_" + str (contador) + ".txt", "w")
            automaton (f, input ("STRING INPUT: "))
            f.close ()
            contador += 1
            print ("\nDONE!\n")
        elif menu_opcion == 2:
            workfile =  input ("FILE NAME: ")
            try:
                fr = open (workfile + ".txt", 'r')
                f = open ("WEBAY_FILE_" + str (contador) + ".txt", "w")
                automaton (f, fr.read())
                fr.close()
                f.close ()
                contador += 1
                print ("\nDONE!\n")
            except:
                print ("\nFILE NOT FOUND\n")
        elif menu_opcion == 3:
            draw_auto()
            print ("\nDONE!\n")
        
#estado inicial
estado = "q1"
cont_ebay = 0
cont_web = 0
contador = 1