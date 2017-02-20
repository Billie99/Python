from math import sqrt

class Punto:
  def __init__(self, x, y):
   self.x = x
   self.y = y

  def distanza_origine(self):
   return sqrt((self.x * self.x) + (self.y * self.y))

