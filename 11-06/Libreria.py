class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

def descrizione(self):
    return "Titolo: " + self.titolo + " | Autore: " + self.autore + " | ISBN: " + self.isbn

class Libreria:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        for l in self.catalogo:
            if l.isbn == libro.isbn:
                print("Il libro con ISBN '" + libro.isbn + "' è già presente nel catalogo.")
                return
        self.catalogo.append(libro)
        print("Libro '" + libro.titolo + "' aggiunto al catalogo.")
    def rimuovi_libro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print("Libro con ISBN '" + isbn + "' rimosso dal catalogo.")
                return
        print("Nessun libro trovato con ISBN '" + isbn + "'.")

    def cerca_per_titolo(self, titolo):
        risultati = [
            libro for libro in self.catalogo
            if titolo.lower() in libro.titolo.lower()
        ]
        return risultati
    def mostra_catalogo(self):
        if not self.catalogo:
            print("Il catalogo è vuoto.")
            return
        for libro in self.catalogo:
            print(libro.descrizione())
        # len() restituisce un numero intero, quindi va convertito in stringa con str()
        print("Totale: " + str(len(self.catalogo)) + " libri")