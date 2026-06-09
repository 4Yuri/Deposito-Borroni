"""Chiedi all'utente di inserire un numero intero positivo n. Se l'utente
inserisce un numero negativo o zero, continua a chiedere un numero fino a
quando non viene inserito un numero positivo."""

def valida_positivo(funzione):
    def wrapper():
        while True:
            numero = funzione()
            if numero > 0:
                return numero
            else:
                print("Numero non valido! Inserisci un numero positivo.")
    return wrapper


@valida_positivo
def chiedi_numero():
    return int(input("Inserisci un numero intero positivo: "))

risultato = chiedi_numero()
print(f"Hai inserito: {risultato}") 