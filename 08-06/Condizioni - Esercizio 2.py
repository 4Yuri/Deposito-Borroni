""" Andare a creare un if con vari elif e un else finale che gestisca un
menu per la selezione di un crud basilare (aggiungi modifica elimina )"""

persone = ["mario, luigi, andrea"]

print("menu")
print("1. aggiungi persona")
print("2. visualizza persone")
print("3. modifica persona")
print("4. elimina persona")
print("0. esci")

scelta = int(input("inserisci la tua scelta:"))

if scelta==1:
    nuova=input("nome persona:")
    persone.append(nuova)
    print("aggiunto")
elif scelta ==2:
    print("persone:")
    print(persone)
elif scelta==3:
    persona=input("a quale persona vuoi cambiare nome?")
    if persona in persone:
        nuovo_nome=input("inserisci nuovo nome:")
        posizione=persone.index(persona)
        persone[posizione]=nuovo_nome
        print("fatto")
    else:
        print("persona non in elenco")
elif scelta==4:
    eliminare=input("inserisci il nome della persona da eliminare")
    if eliminare in persone:
        persone.remove(eliminare)
        print("fatto")
    else:
        print("questa persona non c'è")
elif scelta==0:
    print("ciao")
else:
    print("errore, numero non valido")