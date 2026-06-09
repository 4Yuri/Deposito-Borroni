"""Esercizio Avanzato: Sequenza di Fibonacci fino a N
Descrizione: Chiedi all'utente di inserire un numero N. Il
programma dovrebbe stampare la sequenza di Fibonacci fino a N.
Ad esempio, se l'utente inserisce 100, il programma dovrebbe
stampare tutti i numeri della sequenza di Fibonacci minori o
uguali a 100."""

def fibonacci(n):
    a,b=0,1
    while a<=n:
        print(a)
        a, b = b, a + b


n = int(input("Inserisci un numero N: "))
fibonacci(n)