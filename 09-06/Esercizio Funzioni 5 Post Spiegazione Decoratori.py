
"""Utilizza un ciclo per determinare se un numero è primo. La funzione deve
restituire True se il numero è primo, altrimenti False."""

def e_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Inserisci un numero: "))
print(e_primo(n))