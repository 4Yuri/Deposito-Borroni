"""Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella
lista."""

def somma_pari(lista):
    somma = 0
    for numero in lista:
        if numero % 2 == 0:
            somma += numero
    print(somma)

lista_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somma_pari(lista_numeri)