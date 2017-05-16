import os

numero = 0
num = 0

file = os.path.isfile("sum.dat")

if not file:
   print "Impossibile aprire il file sum.dat, e inesistente "
   exit(0)

else:
    f = open("sum.dat", "r")
    line = f.readline()

    num = int(line)
    f.close()

    print "Lettura del file sum.dat in corso ..."

    print "Valore corrente: ", num
    print " "

    numero = input("Inserisci il valore da sommare ")

    numero = numero + num

    print "Nuovo valore:", numero

    f = open("sum.dat", "w")
    f.write(str(numero))

    print "Salvataggio nel file sum.dat in corso ... "
    print " "

    f.close()
