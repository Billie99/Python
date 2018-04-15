import math

raggio = input("Inserisci il valore del raggio ")

# Superfice della sfera

superficie = (4.0 * math.pi) * (raggio * raggio)
print "Il valore della superfice della sfera e':", superficie

#volume della sfera

volume = (4.0/3.0) * math.pi * (raggio * raggio * raggio)
print "Il volume della sfera e':", volume
