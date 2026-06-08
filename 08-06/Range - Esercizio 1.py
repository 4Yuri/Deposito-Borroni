"""Chiedi all'utente di inserire un numero. Il programma
dovrebbe quindi fare un conto alla rovescia a partire da
quel numero fino a zero, stampando ogni numero e chiederti
se vuoi ripetere o no."""

ripeti = True

while ripeti:
    numero = int(input("Inserisci un numero: "))
    
    while numero <= 0:
        numero = int(input("Errore, inserisci numero maggiore di 0: "))
    
    for i in range(numero, -1, -1):
        print(i)
    
    scelta = input("Vuoi ripetere? (sì/no): ")
    if scelta == "no":
        ripeti = False
    elif scelta=="sì":
        pass
    else:
        scelta=input("Scelta non valida, inserire sì o no:")