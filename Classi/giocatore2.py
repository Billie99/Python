from giocatore import Giocatore

class Giocatore2:
     def __init__(self, nome, punti, munizioni):
	 self.nome = nome
	 self.punti = punti
	 self.munizioni = munizioni
         self.g1 = Giocatore(nome, punti, 10)         

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

     def spara(self):
 	 self.g1.punti = self.g1.punti - 1
     
     def danno(self):
	 return self.g1.punti

      
