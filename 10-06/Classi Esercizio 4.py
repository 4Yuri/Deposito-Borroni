"""Esercizio 4 ():
Crea una classe chiamata Garage. Questa classe dovrebbe avere:
Un attributo di istanza capienza (numero massimo di auto) passato al costruttore.
Un attributo di istanza auto_presenti (lista di stringhe con le targhe), inizialmente vuota.
Un metodo parcheggia che accetti una targa e aggiunga l'auto alla lista. Se il garage è pieno, stampa un messaggio di errore. Se la targa è già presente, avvisa che l'auto è già in garage.
Un metodo rimuovi che accetti una targa e rimuova l'auto corrispondente. Se la targa non è presente, stampa un messaggio di errore.
Un metodo posti_liberi che restituisca il numero di posti ancora disponibili."""

class Garage: # Creo la classe chiamata Garage
    def __init__(self, capienza): # Definisco il metodo costruttore che riceve la capienza massima
        self.capienza = capienza # Salvo la capienza passata come mio attributo interno
        self.auto_presenti = [] # Inizializzo una lista vuota per memorizzare le targhe delle auto

    def parcheggia(self, targa): # Definisco il metodo per parcheggiare, che accetta una targa
        if targa in self.auto_presenti: # Controllo se la targa si trova già nella mia lista di auto
            print("Attenzione: l'auto con targa " + targa + " è già in garage.") # Stampo un avviso per dire che l'auto è già dentro
        elif len(self.auto_presenti) >= self.capienza: # Verifico se il numero di auto ha raggiunto la mia capienza massima
            print("Errore: il garage è pieno, impossibile parcheggiare.") # Stampo un errore perché non ho più posti liberi
        else: # Se l'auto non c'è e ho ancora posto, procedo con il parcheggio
            self.auto_presenti.append(targa) # Aggiungo la nuova targa alla mia lista di auto presenti
            print("Auto con targa " + targa + " parcheggiata con successo.") # Stampo un messaggio per confermare l'avvenuto parcheggio

    def rimuovi(self, targa): # Definisco il metodo per rimuovere un'auto, accettando una targa
        if targa in self.auto_presenti: # Controllo se la targa da rimuovere è effettivamente nella mia lista
            self.auto_presenti.remove(targa) # Rimuovo la targa dalla mia lista di auto presenti
            print("Auto con targa " + targa + " rimossa dal garage.") # Stampo un messaggio per confermare l'avvenuta rimozione
        else: # Se non trovo la targa nella mia lista, eseguo questo blocco
            print("Errore: l'auto con targa " + targa + " non è presente nel garage.") # Stampo un errore perché l'auto che cerco non è nel mio garage

    def posti_liberi(self): # Definisco il metodo per calcolare quanti posti mi sono rimasti
        return self.capienza - len(self.auto_presenti) # Sottraggo il numero di auto attuali dalla mia capienza totale e restituisco il risultato


mio_garage = Garage(2) # Creo un'istanza del mio garage con una capienza massima di 2 posti
mio_garage.parcheggia("AB123CD") # Parcheggio la prima auto nel mio garage
mio_garage.parcheggia("EF456GH") # Parcheggio la seconda auto nel mio garage
mio_garage.parcheggia("IJ789KL") # Provo a parcheggiare una terza auto, ma il mio garage è pieno
mio_garage.parcheggia("AB123CD") # Provo a parcheggiare di nuovo la prima auto, che è già dentro
print("\nPosti liberi attualmente: " + str(mio_garage.posti_liberi())) # Calcolo i miei posti liberi, converto il numero in testo e lo stampo
mio_garage.rimuovi("EF456GH") # Rimuovo la seconda auto dal mio garage
mio_garage.rimuovi("ZZ999ZZ") # Provo a rimuovere un'auto con una targa che non ho nel garage
print("Posti liberi dopo la rimozione: " + str(mio_garage.posti_liberi())) # Ricalcolo e stampo i miei posti liberi aggiornati dopo la rimozione