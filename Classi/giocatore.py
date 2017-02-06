
print "Inizio Gioco "

class Giocatore:
     def __init__(self, nome, punti, munizioni):
         self.nome = nome
         self.punti = punti
         self.munizioni = munizioni

     def imposta_nome(self, nome):
	 self.nome = nome

     def stampa_nome(self):
 	 return self.nome

     def imposta_punti(self, punti):
	 self.punti = punti

     def stampa_punti(self):
	 return self.punti

     def imposta_munizioni(self, munizioni):
	 self.munizioni = munizioni

     def stampa_munizioni(self):
	 return self.munizioni

