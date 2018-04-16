# Calcolo del volume di un cubo o di una sfera
import math

print "Calcolo del volume di un cubo o di una sfera"
scelta = input("Effettua una scelta: (1 - Cubo, 2 - Sfera) ")

if scelta == 1:
# Calcolo del volume di un cubo
   
   lato = input("Inserisci il valore di un lato del cubo: ")
   volume = lato * lato * lato

   print "Il volume del cubo e' :", volume

elif scelta == 2:
# Calcolo del volume di una sfera

     raggio = input("Inserisci il valore del raggio di una sfera ")
     volume = (4.0/3.0) * math.pi * (raggio * raggio * raggio)

     print "Il volume della sfera e':", volume
 
else:
     print "Il numero che hai inserito non esiste"
