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
        # Salvo il mio nome e creo una lista vuota perché devo tenere traccia in modo isolato di tutti gli acquisti che farò personalmente.
        self.nome = nome
        self.acquisti = []

    def compra(self, negozio, nome_articolo, quantita):
        # Verifico se l'articolo esiste nel negozio perché non ha senso provare a comprare qualcosa che non è in vendita.
        if nome_articolo in negozio.inventario:
            articolo = negozio.inventario[nome_articolo]
            costo = articolo.prezzo * quantita
            # Delego al negozio l'aggiornamento del magazzino e dei guadagni perché è lui il proprietario della merce.
            negozio.acquista(nome_articolo, quantita, self.nome)
            # Salvo i dettagli nella mia lista personale per avere una ricevuta storica delle mie spese.
            self.acquisti.append((nome_articolo, quantita, costo))
        else:
            print("Mi dispiace, ma l'articolo non è disponibile nel negozio.")

    def stampa_acquisti(self):
        # Scorro la mia lista personale perché voglio mostrare a schermo esattamente cosa ho comprato e quanto ho speso.
        print("--- Acquisti di", self.nome, "---")
        for a in self.acquisti:
            print("Articolo:", a[0], "| Qta:", a[1], "| Spesa:", a[2])

while True:
    print("NEGOZIO")
    print("1. Registrati")
    print("2. Login")
    print("3. Esci")
    scelta = input("Cosa vuoi fare? ")

    if scelta == "1":
        registra_cliente()

    elif scelta == "2":
        ruolo, utente = login()
        
        if ruolo == "admin":
            # Menu Amministratore
            while True:
                print("Menu Admin")
                print("1. Aggiungi Articolo")
                print("2. Rimuovi Articolo")
                print("3. Vedi Inventario")
                print("4. Rapporto Vendite")
                print("5. Logout")
                scelta_admin = input("Scelta: ")

                if scelta_admin == "1":
                    n = input("Nome articolo: ")
                    p = float(input("Prezzo: "))
                    q = int(input("Quantita: "))
                    nuovo_art = Articolo(n, p, q)
                    negozio.aggiungi_articolo(nuovo_art)
                elif scelta_admin == "2":
                    n = input("Nome articolo da rimuovere: ")
                    negozio.rimuovi_articolo(n)
                elif scelta_admin == "3":
                    negozio.stampa_inventario()
                elif scelta_admin == "4":
                    negozio.rapporto_vendite()
                elif scelta_admin == "5":
                    break

        elif ruolo == "cliente":
            # Menu Cliente
            cliente_attuale = Cliente(utente)
            while True:
                print(" Menu Cliente")
                print("1. Vedi Inventario")
                print("2. Compra Articolo")
                print("3. I miei acquisti")
                print("4. Logout")
                scelta_cliente = input("Scelta: ")

                if scelta_cliente == "1":
                    negozio.stampa_inventario()
                elif scelta_cliente == "2":
                    n = input("Nome articolo da comprare: ")
                    q = int(input("Quanti ne vuoi? "))
                    cliente_attuale.compra(negozio, n, q)
                elif scelta_cliente == "3":
                    cliente_attuale.stampa_acquisti()
                elif scelta_cliente == "4":
                    break

    elif scelta == "3":
        print("Arrivederci!")
        break
