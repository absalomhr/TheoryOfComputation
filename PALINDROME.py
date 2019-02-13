from random import randint

def pali (sizew, israndom, f):
    strw = "P"
    lstrw = ""
    rstrw = ""
    
    f.write ("Rules:\n")
    f.write ("1. P -> epsilon\n2. P -> 0\n3. P -> 1\n4. P -> 0P0\n5. P -> 1P1\n\n")
    
    
    if israndom == True:
        sizew = randint (0, 100000)
        
    f.write ("Size of string: " + str (sizew) + "\n\n")
    f.write ("P\n")
    if sizew % 2 == 0:
        Pvalue = 1
    else:
        Pvalue = randint (2, 3)
    recu = sizew // 2
    for i in range (recu):
        recurule = randint (4, 5)
        if recurule == 4:
            lstrw = lstrw + "0"
            rstrw = "0" + rstrw
            f.write ("(4) " + lstrw + strw + rstrw)
            f.write ("\n")
        else:
            lstrw = lstrw + "1"
            rstrw = "1" + rstrw
            f.write ("(5) " + lstrw + strw + rstrw)
            f.write ("\n")
    if Pvalue == 1:
        strw = "e"
        f.write ("(1) " + lstrw + strw + rstrw)
        f.write ("\n")
    elif Pvalue == 2:
        strw = "0"
        f.write ("(2) " + lstrw + strw + rstrw)
        f.write ("\n")
    else:
        strw = "1"
        f.write ("(3) " + lstrw + strw + rstrw)
        f.write ("\n")
    if strw == "e":
        strw = ""
    f.write ("String w: " + lstrw + strw + rstrw)
    
def run ():
    global contador
    menu_opcion = 0
    while (menu_opcion != 3):
        try:
            menu_opcion = int(input ("MENU:\n\n[1] GENERATE\n[2] CHOOSE SIZE\n[3] EXIT\n\nOPTION : "))
        except:
            menu_opcion = 0
            continue
        if menu_opcion not in range (4):
            continue
        elif menu_opcion == 1:
            f = open ("PALINDROME_GENERATE_" + str (contador) + ".txt", "w")
            pali (-1, True, f)
            f.close ()
            contador += 1
            print ("\nDONE!\n")
        elif menu_opcion == 2:
            f = open ("PALINDROME_USERSIZE_" + str (contador) + ".txt", "w")
            pali (int(input ("\nSELECT SIZE: ")), False, f)
            f.close ()
            contador += 1
            print ("\nDONE!\n")            
contador = 1