"""Scrivi un programma che chieda all'utente di inserire due
numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
per zero, il programma dovrebbe stampare "Errore: Divisione per zero".
Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
non valida"."""

numero1=int(input("inserisci numero 1:"))
numero2=int(input("inserisci numero 2:"))
operazione=input("inserisci operazione:")
match operazione:
    case "+":
        print(numero1+numero2)
    case "-":
        print(numero1-numero2)
    case "*":
        print(numero1*numero2)
    case "/":
        if numero2==0:
            print("errore divisione per 0")
        else:
            print(numero1/numero2)
    case _:
        print("operazione non valida")