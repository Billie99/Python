from punto import *

class Pentagono:

  def __init__(self, P1, P2, P3, P4, P5):

      self.P1 = P1
      self.P2 = P2
      self.P3 = P3
      self.P4 = P4
      self.P5 = P5

  def Area(self):
      return str(abs(1/2 * (self.P3.x - self.P1.x) * (self.P2.y - self.P1.y) - (self.P2.x - self.P1.x) * (self.P3.y - self.P1.y)))

      
