from time import sleep

numero = 0
num = 0

f = open("sum.dat", "r")

if not f:
   print "Impossibile aprire il file sum.dat, e inesistente "
   exit(0)

line = f.readline()

num = int(line)
f.close()

print "Lettura del file sum.dat in corso ..."
sleep(2)

print "Valore corrente: ", num
sleep(2)
print " "

numero = input("Inserisci il valore da sommare ")
sleep(2)

numero = numero + num

print "Nuovo valore:", numero
sleep(2)

f = open("sum.dat", "w")
f.write(str(numero))

print "Salvataggio nel file sum.dat in corso ... "
print " "
sleep(2)

f.close()
