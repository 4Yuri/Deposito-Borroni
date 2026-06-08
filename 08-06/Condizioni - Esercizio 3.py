""" Creare un if con else semplice, dentro l’if inserire una strttura di
creazione di dati ( nome, password, id dato dal sistema a crescere ) e
nell’else il controllo automatico la dove è presente l’accout nel sistema
e solo se si passa dall’else concludere lo script """

utenti=[]
id_corrente = 1
nuovo_utente = input("Vuoi creare un nuovo account? (s/n): ")
if nuovo_utente == "s":
    nome = input("Inserisci il nome: ")
    password = input("Inserisci la password: ")
    
    
    utenti.append((nome, password, id_corrente))
    id_corrente = id_corrente + 1
    print("Account creato con successo!")
else:
    nome_login = input("Inserisci il tuo nome per accedere: ")
    pass_login = input("Inserisci la tua password: ")
    print("Accesso consentito. Programma terminato.")