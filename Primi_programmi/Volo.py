# Programma che determina il tempo di volo di un aeroplano

print "Tempo di volo "
print "Determina la durata massima di volo conoscendo "
print "la quantita' di carburante ed il consumo orario "

carburante = input("Carburante (in galloni): ")
consumo = input("Consumo Orario (in galloni/h): ")

if carburante < 0 or consumo < 0:
   print "Errore la quantita' di carburante e consumo devono essere positivi "

else:
# Calcolo delle ore
     tempo1 = carburante / consumo
     ore = int(tempo1)

# Calcolo dei minuti
     tempo2 = tempo1 - ore
     minuti = int(tempo2 * 60) 

# Calcolo dei secondi
     min = tempo2 * 60
     tempo3 = min - minuti
     secondi = int(tempo3 * 60)

# Un gallone equivale a 3.8 litri
x = input("Inserisci il numero di galloni da convertire in litri ")

galloni = float(x * 3.8)

print "I galloni convertiti in litri sono:", galloni
print "Tempo di volo:", ore ,"h", minuti ,"min", secondi ,"sec" 
