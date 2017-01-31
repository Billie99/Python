# Calcolo del volume di un cubo o di una sfera
import math

print "Calcolo del volume di un cubo o di una sfera"
Scelta = input("Effettua una scelta: (1 - Cubo, 2 - Sfera) ")

if Scelta == 1:
# Calcolo del volume di un cubo
   
   Lato = input("Inserisci il valore di un lato del cubo: ")
   Volume = Lato * Lato * Lato

   print "Il volume del cubo e' :", Volume

elif Scelta == 2:
# Calcolo del volume di una sfera

     pi = math.pi
     Raggio = input("Inserisci il valore del raggio di una sfera ")
     Volume = (4.0/3.0) * pi * (Raggio * Raggio * Raggio)

     print "Il volume della sfera e':", Volume
 
else:
     print "Il numero che hai inserito non esiste"

