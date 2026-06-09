"""Utilizza un ciclo for per stampare tutti i numeri dispari nella lista."""


def stampa_dispari(lista):
    for numero in lista:
        if numero % 2 != 0:
            print(numero)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stampa_dispari(lista)