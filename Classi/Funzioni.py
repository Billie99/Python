# Introduzione alle funzioni 
print "Funzioni in Python "

# Dichiarazione di una funzione
def Somma(a, b):
    c = a + b
    return c

# Input da tastiera
x = input("Inserisci il valore di x ")
y = input("Inserisci il valore di y ")

# Chiamata della funzione Somma restituendo il valore della somma non appena ,
# la funzione viene chiamata 

z = Somma(x, y)

print "Il valore della somma e':" , z
