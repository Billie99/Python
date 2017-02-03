# Introduzione alle classi
print "Classi in Python "

# Dichiarazione della classe e di una funzione speciale "init"
class variabili:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Creazione dell'instanza (Oggetto)
v = variabili(4, 3)

# Stampa dei valori
print "Il primo valore e':", v.x
print "Il secondo valore e':", v.y
