"""Esercizio 7
Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
1. Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
2. Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
3. Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto."""

class Piatto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
    def descrizione(self):
        return self.nome + " - " + str(self.prezzo) + " euro"

class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        # Attributo che indica se il ristorante è aperto o chiuso
        self.aperto = False
        self.menu = []

    def descrivi_ristorante(self):
        print("Il ristorante", self.nome, "offre cucina", self.tipo_cucina)
    def stato_apertura(self):
        if self.aperto == True:
            print("Il ristorante", self.nome, "è aperto")
        else:
            print("Il ristorante", self.nome, "è chiuso")
    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante", self.nome, "è ora aperto")
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante", self.nome, "è ora chiuso!")
    def aggiungi_al_menu(self, piatto):
        # Aggiungiamo l'oggetto Piatto alla lista menu
        self.menu.append(piatto)
        print("Aggiunto al menu:", piatto.nome)
    def togli_dal_menu(self, nome_piatto):
        # Cerchiamo il piatto nella lista confrontando i nomi
        trovato = False
        for piatto in self.menu:
            if piatto.nome == nome_piatto:
                c=1
                self.menu.remove(piatto)
                print("Rimosso dal menu:", nome_piatto)
                trovato = True
            
        if trovato == False:
            print("Il piatto", nome_piatto, "non è presente nel menu")
    def stampa_menu(self):
        if len(self.menu) == 0:
            print("Il menu è vuoto!")
        else:
            # Per ogni oggetto Piatto nella lista, chiamiamo il suo metodo descrizione()
            for piatto in self.menu:
                print("-", piatto.descrizione())

ristorante1 = Ristorante("Da Mario", "Italiana")
ristorante1.descrivi_ristorante()
piatto1 = Piatto("Pizza Margherita", 8.00)
piatto2 = Piatto("Spaghetti alla Carbonara", 12.00)
piatto3 = Piatto("Lasagne", 10.50)
piatto4 = Piatto("Tiramisù", 5.00)
ristorante1.apri_ristorante()
ristorante1.stato_apertura()
ristorante1.aggiungi_al_menu(piatto1)
ristorante1.aggiungi_al_menu(piatto2)
ristorante1.aggiungi_al_menu(piatto3)
ristorante1.aggiungi_al_menu(piatto4)
ristorante1.stampa_menu()
ristorante1.togli_dal_menu("Lasagne")
ristorante1.togli_dal_menu("Bistecca")  # Piatto non presente
ristorante1.stampa_menu()
ristorante1.chiudi_ristorante()
ristorante1.stato_apertura()