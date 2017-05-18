import os
import time

numero = 0
num = 0

file = os.path.isfile("sum.dat")

if not file:

   print "Impossibile aprire il file sum.dat, e' inesistente "
   time.sleep(2)
   print "Verra creato un nuovo file"
   time.sleep(2)

else:
    f = open("sum.dat", "r")
    line = f.readline()

    num = int(line)
    f.close()

print "Lettura del file sum.dat in corso ..."
time.sleep(2)
print "Valore corrente: ", num
print " "
time.sleep(2)

numero = input("Inserisci il valore da sommare ")

numero = numero + num
print "Nuovo valore:", numero
time.sleep(2)	

f = open("sum.dat", "w")
f.write(str(numero))

print "Salvataggio nel file sum.dat in corso ... "
print " "

f.close()
