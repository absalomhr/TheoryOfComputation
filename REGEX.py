from random import randint

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

def regex2 ():
    #partes de la cadena
    parte1 = ""
    parte2 = ""
    
    #calculo de parte 1: [(10)*0 + 1(01)*1]
    flag = randint (0, 1000)
    subparte1 = "10" * flag + "0"
    flag = randint (0, 1000)
    subparte2 = "1" + "01" * flag + "1"
    flag = randint (1, 2)
    if flag == 1:
        parte1 = subparte1
    elif flag == 2:
        parte1 = subparte2
    
    #calculo de parte 2: [(0(01)*(1 + 00) + 1(10)*(0 + 11))]*
    #0(01)*(1 + 00)
    flag = randint (0, 1000)
    subparte1 = "0" + "01" * flag
    flag = randint (1, 2)
    if flag == 1:
        subparte1 = subparte1 + "1"
    elif flag == 2:
        subparte1 = subparte1 + "00"
    #1(10)*(0 + 11))
    flag = randint (0, 1000)
    subparte2 = "1" + "10" * flag
    flag = randint (1, 2)
    if flag == 1:
        subparte2 = subparte2 + "0"
    elif flag == 2:
        subparte2 = subparte2 + "11"
    flag = randint (1, 2)
    if flag == 1:
        parte2 = subparte1
    elif flag == 2:
        parte2 = subparte2
    flag = randint (0, 1000)
    #cadena generada
    return parte1 + (parte2 * flag)

def run ():
    global contador
    menu_opcion = 0
    while (menu_opcion != 3):
        try:
            menu_opcion = int(input ("MENU:\n\n[1] REGEX 1\n[2] REGEX 2\n[3] EXIT\n\nOPTION : "))
        except:
            menu_opcion = 0
            continue
        if menu_opcion not in range (4):
            continue
        elif menu_opcion == 1:
            f = open ("REGEX1_" + str (contador) + ".txt", "w")
            for i in range (5):
                f.write ("REGEX: " + str (i + 1) + "\n")
                f.write (regex1 ())
                f.write ("\n")
            f.close ()
            contador += 1
            print ("\nDONE!\n")
        elif menu_opcion == 2:
            f = open ("REGEX2_" + str (contador) + ".txt", "w")
            for i in range (5):
                f.write ("REGEX: " + str (i + 1) + "\n")
                f.write (regex2 ())
                f.write ("\n")
            f.close ()
            contador += 1
            print ("\nDONE!\n")            
contador = 1

   