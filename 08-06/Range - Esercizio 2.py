"""Chiedi all'utente di inserire un numero.
Il programma dovrebbe controllare se il numero inserito è
primo / pari o no. Se è primo, lo salva e stampa "Il numero
è primo"
. Altrimenti, stampa "Il numero non è primo"
.
si ferma il tutto quando ha 5 numeri primi"""



ripeti=True
while ripeti:
    numero=int(input("Inserisci un numero:"))
    count=0
    if numero/2==0:
        print("pari")
        count+=1
    else:
        print("dispari")
    if count==5:
        ripeti=False