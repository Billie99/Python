from punto import *

class Triangolo:
  def __init__(self, P1, P2, P3):

      self.P1 = P1
      self.P2 = P2
      self.P3 = P3

  def Area(self):

      return (str(1/2 * (self.P3.x - self.P1.x) * (self.P2.y - self.P1.y) - (self.P2.x - self.P1.x) * (self.P3.y - self.P1.y)))

    

