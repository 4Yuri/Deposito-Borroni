"""Descrizione: Scrivi un programma che chieda all'utente di inserire un numero
intero positivo n. Il programma deve poi eseguire le seguenti operazioni:
1.Utilizzare un ciclo while per garantire che l'utente inserisca un numero
positivo. Se l'utente inserisce un numero negativo o zero, il programma deve
continuare a chiedere un numero fino a quando non viene inserito un numero
positivo.
2.Utilizzare un ciclo for con range per calcolare e stampare la somma dei
numeri pari da 1 a n.
3.Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
4.Utilizzare una struttura if per determinare se n è un numero primo. Un numero
primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se
n è primo o no.
5.Stampare tutto"""

"""plus: non funziona su un numero singolo ma su una lista"""

n = int(input("Inserisci un numero intero: "))
while n <= 0:
    n = int(input("Il numero deve essere positivo. Riprova: "))

while n > 0:
    somma = 0
    for i in range(2, n + 1, 2):
        somma += i
    print("La somma dei numeri pari è:", somma)

    for i in range(1, n + 1, 2):
        print(i)

    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False

    if primo and n > 1:
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

    n = int(input("Inserisci un numero intero: "))
    while n <= 0:
        n = int(input("Il numero deve essere positivo. Riprova: "))