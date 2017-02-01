# Equazioni di secondo grado

import math

a = input("Inserisci il valore di a ") # Coefficiente della x^2
b = input("Inserisci il valore di b ") # Coefficiente della x
c = input("Inserisci il valore di c ") # Termine noto

if a == 0 and b == 0 and c == 0:
   print "L'equazione ammette infinite soluzioni "

elif a == 0 and b == 0: 
     print "L'equazione non ammette soluzioni "

elif a == 0:
     print "L'equazione e' di primo grado "

     x = -float(c) / float(b)
     print "Il risultato dell'equazione e':", x

else:
# Troviamo il Discriminante

     delta = (b * b) - (4 * (a) * (c))
     print "Abbiamo trovato il delta che e':",delta
     

if delta < 0:

# Discriminante minore di 0

   print "L'equazione non ammette soluzioni reali e distinte "

elif delta == 0:
# Discriminante = 0

     x = -float(b) / (2.0 * a)
     print "L'equazione ammette due soluzioni coincidenti quindi x1 = x:", x

else:
# Discriminante maggiore di 0
    
     print "L'equazione ammette due soluzioni reali e distinte "
     radice = math.sqrt(delta)
     x1 = ((-float (b)) + math.sqrt(delta) / (2.0 * float(a)))
     x2 = ((-float (b)) - math.sqrt(delta) / (2.0 * float(a)))

     print "Le soluzioni dell'equazione sono:",x1,"e",x2 
