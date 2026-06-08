"""Scrivi un programma che chieda all'utente la sua età. Se l'età è
inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi
vedere questo film".
Altrimenti, dovrebbe stampare "Puoi vedere questo film"""


età = int(input("Inserisci la tua età: "))

match età:
    case _ if età < 18:
        print("Mi dispiace, non puoi vedere questo film")
    case _ if età >= 18:
        print("Puoi vedere questo film")
    case _:
        print("errore")