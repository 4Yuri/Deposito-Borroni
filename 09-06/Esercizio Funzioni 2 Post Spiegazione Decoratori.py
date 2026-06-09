"""Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza
della lista deve essere n.
"""


import random

def genera_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1, n))
    return lista

n = int(input("Inserisci n: "))
print(genera_lista(n))