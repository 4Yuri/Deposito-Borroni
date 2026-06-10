"""Esercizio 3 (Medio):
Crea una classe chiamata ContoCorrente. Questa classe dovrebbe avere:
Due attributi di istanza: intestatario e saldo (il saldo iniziale deve essere passato al costruttore, con valore di default 0).
Un metodo deposita che accetti un importo e lo aggiunga al saldo. Se l'importo è negativo o zero, stampa un messaggio di errore senza modificare il saldo.
Un metodo preleva che accetti un importo e lo sottragga dal saldo. Se il saldo non è sufficiente, stampa un messaggio di errore senza modificare il saldo.
Un metodo stampa_saldo che stampi una stringa del tipo "Il saldo di 'intestatario' è: 'saldo' €"."""

class ContoCorrente:
    def __init__(self, intestatario, saldo=0):
        self.intestatario = intestatario
        self.saldo = saldo
    def deposita(self, importo):
        if importo <= 0:
            print("Errore: l'importo da depositare deve essere maggiore di zero")
        else:
            self.saldo += importo
    def preleva(self, importo):
        if importo <= 0:
            print("Errore: l'importo da prelevare deve essere maggiore di zero")
        elif importo > self.saldo:
            print("Errore: saldo non sufficiente per questo prelievo")
        else:
            self.saldo -= importo
    def stampa_saldo(self):
        print("Il saldo di " + self.intestatario + " è: " + str(self.saldo) + " €")

conto_mario = ContoCorrente("Stefania Botti")
conto_mario.stampa_saldo()
conto_mario.deposita(100)
conto_mario.stampa_saldo()
conto_mario.preleva(150)