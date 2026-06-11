"""Esercizio 5 (Facile) @staticmethod:
Crea una classe chiamata Convertitore. Questa classe dovrebbe avere:
Un metodo statico euro_in_dollari che accetti un importo in euro e restituisca il valore convertito in dollari, usando un tasso fisso di 1.08.
Un metodo statico km_in_miglia che accetti una distanza in chilometri e restituisca il valore convertito in miglia, usando un fattore fisso di 0.621371.
Testa la classe chiamando entrambi i metodi direttamente dalla classe, senza creare alcun oggetto."""

class Convertitore:
    # Metodo statico per convertire euro in dollari
    @staticmethod
    def euro_in_dollari(importo_euro):
        # Definizione del tasso di cambio fisso euro -> dollari
        TASSO_CAMBIO = 1.08
        # Calcolo della conversione moltiplicando l'importo per il tasso
        importo_dollari = importo_euro * TASSO_CAMBIO
        # Ritorno del risultato della conversione
        return importo_dollari
    # Metodo statico per convertire chilometri in miglia
    @staticmethod
    def km_in_miglia(distanza_km):
        # Definizione del fattore di conversione fisso km -> miglia
        FATTORE_CONVERSIONE = 0.621371
        # Calcolo della conversione moltiplicando la distanza per il fattore
        distanza_miglia = distanza_km * FATTORE_CONVERSIONE
        # Ritorno del risultato della conversione
        return distanza_miglia
    
# Primo test: conversione di 100 euro
# Chiamo il metodo direttamente dalla classe Convertitore (senza creare oggetti)
euro1 = 100
dollari1 = Convertitore.euro_in_dollari(euro1)
# Uso la virgola nel print per stampare testo e variabili insieme
# La virgola aggiunge automaticamente uno spazio tra gli elementi
print(euro1, "euro equivalgono a", dollari1, "dollari")