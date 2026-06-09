"""Punto 1: Utilizzo di if
Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari
e "Dispari" se il numero è dispari.
Punto 2: Utilizzo di while e range
Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i
numeri da n a 0 (compreso), decrementando di 1.Deve potersi ripete all’infinito
Punto 3: Utilizzo di for
Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
ciascun numero nella lista.
Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema che prende in input
una lista di numeri interi che precedentemente è stata valorizzata dall’utente.
Il sistema deve:
1.Utilizzare un ciclo for per trovare il numero massimo nella lista.
2.Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
3.Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
altrimenti stampare il numero massimo trovato e il numero di elementi nella lista"""

while True:
    print("MENU PRINCIPALE")
    print("1. Pari o Dispari (if)")
    print("2. Countdown (while e range)")
    print("3. Quadrati di una lista (for)")
    print("4. Analisi lista interi (if, while, for)")
    print("5. Esci dal programma")
    
    scelta_testo = input("Scegli un numero tra 1 e 5: ")
    while scelta_testo != "1" and scelta_testo != "2" and scelta_testo != "3" and scelta_testo != "4" and scelta_testo != "5":
        print("Errore: devi inserire un numero valido tra 1 e 5!")
        scelta_testo = input("Scegli un numero tra 1 e 5: ")
        
    scelta = int(scelta_testo)
        
    match scelta:
        case 1:
            ripetere = True
            while ripetere:
                numero = float(input("inserisci un numero: "))
                if numero % 2 == 0:
                    print("Pari")
                else:
                    print("Dispari")
                    
                scelta1 = input("vuoi ripetere l'esecuzione? sì o no: ")
                if scelta1 == "sì":
                    pass
                elif scelta1 == "no":
                    ripetere = False
                else:
                    while scelta1 != "sì" and scelta1 != "no":
                        scelta1 = input("inserisci una scelta valida: sì o no: ")
                    if scelta1 == "no":
                        ripetere = False
                        
        case 2:
            ripetere = True
            while ripetere:
                n = int(input("inserisci un numero intero positivo: "))
                for i in range(n, -1, -1):
                    print(i)
                    
                scelta1 = input("vuoi ripetere l'esecuzione? sì o no: ")
                if scelta1 == "sì":
                    pass
                elif scelta1 == "no":
                    ripetere = False
                else:
                    while scelta1 != "sì" and scelta1 != "no":
                        scelta1 = input("inserisci una scelta valida: sì o no: ")
                    if scelta1 == "no":
                        ripetere = False
                        
        case 3:
            ripetere = True
            while ripetere:
                lista = []
                continua = "sì"
                while continua == "sì":
                    numero = float(input("inserisci un numero: "))
                    lista.append(numero)
                    continua = input("vuoi inserire un altro numero? sì o no: ")
                    
                print("ecco i quadrati:")
                for numero in lista:
                    print(numero ** 2)
                    
                scelta1 = input("vuoi ripetere l'esecuzione? sì o no: ")
                if scelta1 == "sì":
                    pass
                elif scelta1 == "no":
                    ripetere = False
                else:
                    while scelta1 != "sì" and scelta1 != "no":
                        scelta1 = input("inserisci una scelta valida: sì o no: ")
                    if scelta1 == "no":
                        ripetere = False
                        
        case 4:
            ripetere = True
            while ripetere:
                lista = []
                continua = "sì"
                while continua == "sì":
                    numero = int(input("inserisci un numero intero: "))
                    lista.append(numero)
                    continua = input("vuoi inserire un altro numero? sì o no: ")
                
                
                a = lista[0]
                for i in lista:
                    if i > a:
                        a = i
                
                print("il massimo è " + str(a))
                
                
                contatore = 0
                indice = 0
                while indice < len(lista):
                    contatore += 1
                    indice += 1
                
                print(contatore)
                """manca il 3"""
                scelta1 = input("vuoi ripetere l'esecuzione? sì o no: ")
                if scelta1 == "sì":
                    pass
                elif scelta1 == "no":
                    ripetere = False
                else:
                    while scelta1 != "sì" and scelta1 != "no":
                        scelta1 = input("inserisci una scelta valida: sì o no: ")
                    if scelta1 == "no":
                        ripetere = False
                        
        case 5:
            print("Programma terminato")
            break
            
        case _:
            print("Errore: scelta non valida")