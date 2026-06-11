"""Esercizio 6 (Facile) @classmethod:
Crea una classe chiamata Animale. Questa classe deve avere:
Un attributo di classe numero_animali, inizializzato a 0.
Due attributi di istanza: nome e specie, passati al costruttore.
Il costruttore deve incrementare numero_animali di 1 ogni volta che viene creato un nuovo animale.
Un metodo di classe quanti_animali che stampi una stringa del tipo "Numero di animali creati: 'numero_animali'".
Crea almeno 3 oggetti Animale e poi chiama quanti_animali direttamente dalla classe, senza usare nessuna delle istanze create."""


class Animale:
    # ATTRIBUTO DI CLASSE
    # Appartiene alla classe stessa, NON ai singoli oggetti
    numero_animali = 0
    # COSTRUTTORE della classe (chiamato ogni volta che si crea un nuovo oggetto)
    # 'self' rappresenta l'oggetto che stiamo creando
    # 'nome' e 'specie' sono i dati che passiamo quando creiamo un animale
    def __init__(self, nome, specie):
        # ATTRIBUTI DI ISTANZA
        self.nome = nome
        self.specie = specie
        # Ogni volta che creiamo un animale, il contatore sale di 1
        Animale.numero_animali += 1
    # METODO DI CLASSE con il decoratore @classmethod
    # 'cls' è come 'self' ma si riferisce alla classe invece che all'oggetto
    # Può essere chiamato direttamente dalla classe senza creare oggetti
    @classmethod
    def quanti_animali(cls):
        print("Numero di animali creati:", cls.numero_animali)

# Creo il primo oggetto Animale
animale1 = Animale("Fido", "Cane")
print("Creato:", animale1.nome, "di specie", animale1.specie)
# Creo il secondo oggetto Animale
animale2 = Animale("Whiskers", "Gatto")
print("Creato:", animale2.nome, "di specie", animale2.specie)
# Chiamo il metodo di classe DIRETTAMENTE dalla classe
Animale.quanti_animali()