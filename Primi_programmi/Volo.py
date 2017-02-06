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
     tempo_ore = carburante / consumo
     ore = int(tempo_ore)

# Calcolo dei minuti
     tempo_minuti = tempo_ore - ore
     minuti = int(tempo_minuti * 60) 

# Calcolo dei secondi
     min = tempo_minuti * 60
     tempo_secondi = min - minuti
     secondi = int(tempo_secondi * 60)

# Un gallone equivale a 3.8 litri

print "I galloni convertiti in litri sono:", galloni
print "Tempo di volo:", ore ,"h", minuti ,"min", secondi ,"sec" 
