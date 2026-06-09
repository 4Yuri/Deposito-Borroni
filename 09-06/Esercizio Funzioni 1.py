"""Descrizione: Scrivi un programma che genera un numero casuale
tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è
stato generato. Dopo ogni tentativo, il programma dovrebbe
dire all'utente se il numero da indovinare è più alto o più
basso rispetto al numero inserito. Il gioco termina quando
l'utente indovina il numero o decide di uscire."""

import random

def genera_numero():
    return random.randint(1, 100)

def ottieni_tentativo():
    indovina = int(input("Inserisci un numero (1-100): "))
    while indovina < 1 or indovina > 100:
        indovina = int(input("Numero non valido. Riprova (1-100): "))
    return indovina

def confronta_numero(tentativo, segreto):
    if tentativo < segreto:
        print("Il numero da indovinare è più alto.")
        return False
    elif tentativo > segreto:
        print("Il numero da indovinare è più basso.")
        return False
    else:
        print("Esatto, hai indovinato.")
        return True
    
def gioca():
    segreto = genera_numero()
    print("Ho generato un numero")
    while True:
        scelta = input("Premi Invio per fare un tentativo, oppure scrivi 'esci' per abbandonare: ")
        if scelta.lower() == 'esci':
            print("Hai scelto di uscire. Il numero segreto era "+segreto)
            break
        n = ottieni_tentativo()
        if confronta_numero(n, segreto):
            break

gioca()