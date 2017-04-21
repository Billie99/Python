class Lista:
  def __init__(self):
      self.lista = []

l = Lista()

i = 0;
while i < 100:

      i = i + 1
      l.lista.append(i)

print l.lista
