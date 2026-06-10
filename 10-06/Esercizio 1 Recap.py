"""Scrivere un programma per l'analisi delle temperature settimanali. Il programma deve permettere di:

inserire le temperature in una lista
calcolare la media e contare i giorni sotto zero
filtrare i dati e mostrare le sole temperature positive
(extra) decoratore per stampare un messaggio di inizio e fine elaborazione
uscire dal programma"""


def decoratore_elaborazione(funzione):
    def wrapper(*args, **kwargs):
        print("Inizio Elaborazione")
        funzione(*args, **kwargs)
        print("Fine Elaborazione")
    return wrapper

@decoratore_elaborazione
def analizza_temperature(lista_temp):
    if len(lista_temp) == 0:
        print("Nessuna temperatura inserita. Torna al menu 1")
    else:
        somma = 0
        sotto_zero = 0
        
        for temp in lista_temp:
            somma += temp
            if temp < 0:
                sotto_zero += 1
                
        media = somma / len(lista_temp)
        
        print("La media delle temperature e:", media)
        print("I giorni con temperatura sotto zero sono stati:", sotto_zero)

def genera_positive(lista_temp):
    for temp in lista_temp:
        if temp > 0:
            yield temp

temperature = []

while True:
    print("Analizzatore di Temperature")
    print("1. Inserisci temperature")
    print("2. Calcola media e conta giorni sotto zero")
    print("3. Mostra temperature positive")
    print("4. Esci dal programma")
    
    scelta = input("Seleziona un'opzione (1-4): ")
    
    match scelta:
        case '1':
            num_giorni = int(input("Quante temperature vuoi inserire? "))
            for i in range(num_giorni):
                print("Inserisci la temperatura del giorno", i + 1)
                temp = float(input())
                temperature.append(temp)
            print("Temperature salvate in memoria")
            
        case '2':
            analizza_temperature(temperature)
            
        case '3':
            if len(temperature) == 0:
                print("Nessuna temperatura inserita. Torna al menu 1")
            else:
                print("Temperature positive trovate:")
                trovate = 0
                for temp_positiva in genera_positive(temperature):
                    print(temp_positiva)
                    trovate += 1
                    
                if trovate == 0:
                    print("Non ci sono temperature positive.")
            
        case '4':
            print("Uscita dal programma")
            break
            
        case _:
            print("Opzione non valida")