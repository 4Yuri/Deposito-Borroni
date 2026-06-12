class Articolo:
    def __init__(self, nome, prezzo, quantita):
        # Inizializzo nome, prezzo e quantità 
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def aggiungi(self, qta):
        # Aumento la quantità in magazzino
        self.quantita += qta

    def rimuovi(self, qta):
        # Diminuisco la quantità e restituisco True o False - chi mi chiama deve sapere se c'era abbastanza merce per completare l'operazione
        if self.quantita >= qta:
            self.quantita -= qta
            return True
        return False

    def aggiorna_prezzo(self, nuovo_prezzo):
        # Modifico il prezzo
        self.prezzo = nuovo_prezzo

    def stampa_info(self):
        # Mostro a schermo i miei dettagli
        print("Prodotto:", self.nome, "Prezzo:", self.prezzo, "Quantita:", self.quantita)


class Negozio:
    def __init__(self, nome):
        # Creo il nome del negozio, un dizionario vuoto per l'inventario, una lista per le vendite e il guadagno a zero per iniziare a gestire l'attività
        self.nome = nome
        self.inventario = {}
        self.storico_vendite = []
        self.guadagno_totale = 0

    def aggiungi_articolo(self, articolo):
        # Inserisco l'articolo nel mio dizionario usando il nome come chiave
        self.inventario[articolo.nome] = articolo
        print("Articolo aggiunto al catalogo:", articolo.nome)

    def rimuovi_articolo(self, nome_articolo):
        # Elimino l'articolo dal dizionario 
        if nome_articolo in self.inventario:
            del self.inventario[nome_articolo]
            print("Articolo rimosso dal catalogo.")
        else:
            print("Articolo non trovato.")

    def acquista(self, nome_articolo, quantita, cliente):
        # Gestisco qui l'acquisto perché sono io (il Negozio) che devo scalare la merce, calcolare il ricavo e registrare la transazione nel mio storico centrale
        if nome_articolo in self.inventario:
            articolo = self.inventario[nome_articolo]
            if articolo.rimuovi(quantita):
                costo = articolo.prezzo * quantita
                self.guadagno_totale += costo
                self.storico_vendite.append((cliente, nome_articolo, quantita, costo))
                print("Acquisto riuscito:", quantita, "pezzi di", nome_articolo, "per", cliente)
            else:
                print("Quantita insufficiente in magazzino")
        else:
            print("Articolo non disponibile")

    def stampa_inventario(self):
        # Scorro tutti i valori del mio dizionario per mostrare l'elenco di ciò che è attualmente in vendita
        print("Inventario")
        for articolo in self.inventario.values():
            articolo.stampa_info()

    def rapporto_vendite(self):
        # Leggo il mio storico vendite perché l'amministratore deve vedere sia il profitto totale sia il dettaglio di ogni singola transazione avvenuta
        print("Rapporto Vendite")
        print("Guadagno Totale:", self.guadagno_totale)
        for vendita in self.storico_vendite:
            print("Cliente:", vendita[0], "Articolo:", vendita[1], "Qta:", vendita[2], "Ricavo:", vendita[3])

class Cliente:
    def __init__(self, nome):
        # Salvo il mio nome e creo una lista vuota
        self.nome = nome
        self.acquisti = []

    def compra(self, negozio, nome_articolo, quantita):
        # Chiedo al negozio di processare l'acquisto e poi salvo la ricevuta nella mia lista perché voglio avere un mio storico personale delle spese sostenute
        if nome_articolo in negozio.inventario:
            articolo = negozio.inventario[nome_articolo]
            costo = articolo.prezzo * quantita

    def stampa_acquisti(self):
        # Scorro la mia lista personale per mostrare a schermo cosa ho comprato e quanto ho speso.
        print("Acquisti di", self.nome)
