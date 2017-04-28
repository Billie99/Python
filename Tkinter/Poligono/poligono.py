from triangolo import *
from punto import *

class Poligono:
   def __init__(self, punti, PuntoMedio):

       self.somma = 0
       self.punti = punti
       self.PuntoMedio = PuntoMedio

   def Area(self):
       
       Numpunti = len(self.punti)

       if Numpunti == 6:

          self.somma = 0

          for i in range(len(self.punti) - 1):
              tr = Triangolo(self.PuntoMedio, self.punti[i], self.punti[i+1])
              self.somma = self.somma + float(tr.Area())
       
          return self.somma   

       elif Numpunti == 5:

            self.somma = 0

            for i in range(len(self.punti) - 2):
                tr = Triangolo(self.PuntoMedio, self.punti[i], self.punti[i+1])
                self.somma = self.somma + float(tr.Area())

            return self.somma
  

            
 
