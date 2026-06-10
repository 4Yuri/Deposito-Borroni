"""Esercizio 2 (Facile):
Crea una classe chiamata Libro.
Questa classe dovrebbe avere:
Tre attributi: titolo, autore e pagine.
Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".
Extra: permetti di creare quanti libri vuole l’utente"""

class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return "Il libro '" + self.titolo + "' è stato scritto da '" + self.autore + "' e ha " + str(self.pagine) + " pagine."
    
libreria = []

while True:
    risposta = input("Vuoi inserire un nuovo libro? (sì/no): ")
    if risposta.lower() != "sì" and risposta.lower() != "si":
        break

    t = input("Inserisci il titolo: ")
    a = input("Inserisci l'autore: ")
    p = input("Inserisci il numero di pagine: ")

    nuovo_libro = Libro(t, a, int(p))
    libreria.append(nuovo_libro)

    print(nuovo_libro.descrizione())