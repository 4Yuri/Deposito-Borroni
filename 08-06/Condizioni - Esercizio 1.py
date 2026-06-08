""" es1"""
""" Creare una serie di condizioni una dentro l’altra che a fronte di un
imput per ogni if decidano se farti passare o no ( 3 livelli, fate un
paragone con == )"""


eta=int(input("inserisci la tua età:"))

if (eta >18):
    print("sei maggiorenne, puoi passare")
elif eta<18:
    print("non puoi passare, sei minorenne")
else:
    print("hai 18 anni, puoi passare");