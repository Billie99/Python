from triangolo import *
from quadrato import *
from pentagono import *

class Medio:    

  def __init__(self, triangolo, quadrato, pentagono):

      self.triangolo = triangolo
      self.quadrato = quadrato
      self.pentagono = pentagono

  def Medio_tr(self):

      ym = (float(self.triangolo.P1.y) + float(self.triangolo.P2.y) + float(self.triangolo.P3.y)) / 3.0  
      xm = (float(self.triangolo.P1.x) + float(self.triangolo.P2.x) + float(self.triangolo.P3.x)) / 3.0

      return str("(" + "xm = " + str(xm) + " " + "," + " " + "ym = " + str(ym) + ")") 
 

  def Medio_q(self):

      xm = (float(self.quadrato.P1.x) + float(self.quadrato.P2.x) + float(self.quadrato.P3.x) + float(self.quadrato.P4.x)) / 4.0
      ym = (float(self.quadrato.P1.y) + float(self.quadrato.P2.y) + float(self.quadrato.P3.y) + float(self.quadrato.P4.y)) / 4.0

      return str("(" + "xm = " + str(xm) + " " + "," + " " + "ym = " + str(ym) + ")")


  def Medio_p(self):

      xm = (float(self.pentagono.P1.x) + float(self.pentagono.P2.x) + float(self.pentagono.P3.x) 
            + float(self.pentagono.P4.x) + float(self.pentagono.P5.x)) / 5.0

      ym = (float(self.pentagono.P1.y) + float(self.pentagono.P2.y) + float(self.pentagono.P3.y) 
            + float(self.pentagono.P4.y) + float(self.pentagono.P5.y)) / 5.0


      return str("(" + "xm = " + str(xm) + " " + "," + " " + "ym = " + str(ym) + ")")
