from triangolo import *
from quadrato import *

class Punto:

  def __init__(self, x, y):

      self.x = x
      self.y = y

  def medio(punti):

      numPunti = len(punti)

      somma = 0
      somma1 = 0

      for i in range(numPunti):

          somma = somma + punti[i].x
          somma1 = somma1 + punti[i].y

      xm = (float(somma) / float(numPunti))
      ym = (float(somma1) / float(numPunti))

      return str("(" + "xm = " + str(xm) + " " + "," + " " + "ym = " + str(ym) + ")")


 
            



