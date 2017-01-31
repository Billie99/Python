# Equazione di primo grado
# ax + b = 0

print "Equazioni di primo grado "

a = input("Inserisci il valore di a ")
b = input("Inserisci il valore di b ")

if a == 0 and b == 0:
   print "L'equazione e' indeterminata"

elif a == 0:
     print "L'equazione e' impossibile"

else:
     x = -float(b) / float(a)
     print "Il valore della x e':", x
