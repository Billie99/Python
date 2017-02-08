import time
from giocatore import Giocatore

nome = raw_input("Inserisci nome del giocatore -> ")

g1 = Giocatore(nome, 10, 10)
g1.imposta_nome(nome)

print " "

print "Il nome del giocatore e':", g1.stampa_nome()
print "Punti iniziali:", g1.punti
print "Fulmini:", g1.munizioni

print " "

nome = raw_input("Inserisci il nome del secondo giocatore -> ")

g2 = Giocatore(nome, 10, 10)
g2.imposta_nome(nome)
print " "

print "Il nome del secondo giocatore e':", g2.stampa_nome()
print "Punti iniziali:", g2.punti
print "Palle di fuoco:", g2.munizioni

print " "
time.sleep(3)

print "Il Giocatore selezionato e':", g2.stampa_nome()
print " "

a = raw_input("Vuoi sparare ? (si , no) ")

if a == "si" or a == "s":
   g2.spara()

else:
     print "GAME OVER "
     print "Il vincitore e':", g1.stampa_nome()
     exit(0)
   
time.sleep(1)

print "Il Giocatore", g1.stampa_nome() , "e' stato colpito!" 
print "Totale punti:", g2.stampa_punti()

print " "

time.sleep(4)
print "Il Giocatore" ,g1.stampa_nome() , "e' stato colpito di nuovo!"

for i in range(3):
    g2.spara()

print "Totale punti:", g2.stampa_punti()   

print " "

time.sleep(4)
print "Il Giocatore" ,g1.stampa_nome() , "sta per morire!"

for i in range(4):
    g2.spara()

print "Totale punti:", g2.stampa_punti()

print " "
print g1.stampa_nome(), "e' troppo debole per attaccare!"

print " "
time.sleep(4)

print g1.stampa_nome(), "e' morto "
for i in range(2):
    g2.spara()

print "Totale punti:", g2.stampa_punti()

print " "

time.sleep(3)
print "GAME OVER "
print "Hai vinto! Il vincitore e':", g2.stampa_nome()
