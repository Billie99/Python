from tkinter import *

class Finestra(Tk):
  def __init__(self):
      Tk.__init__(self)
      self.title("Calcolatrice")
      self.config(bg = "green")
      self.geometry("323x200")
  
      self.numero = IntVar()
      self.numero1 = IntVar()
      self.risultato = IntVar()

      Label(width = 40, text = "Calcolatrice").grid(
      column = 0, row = 0, sticky = 'nsew')
  
      Label(width = 13, text = "Numero 1").grid(
      column = 0, row = 1, sticky = 'w')

      Entry(width = 10, textvariable = self.numero).grid(
      column = 0, row = 2, sticky = 'w')

      Label(width = 13, text = "Numero 2").grid(
      column = 0, row = 1, sticky = 'e')

      Entry(width = 10, textvariable = self.numero1).grid(
      column = 0, row = 2, sticky = 'e')

      Button(width = 10, text = "Somma", command = self.somma).grid(
      column = 0, row = 2, sticky = 'n')

      Label(width = 10, textvariable = self.risultato).grid(
      column = 0, row = 6, sticky = 'e')

      Button(width = 10, text = "Cancella", command = self.cancella).grid(
      column = 0, row = 0, sticky = 'w')

      Button(width = 10, text = "Esci", command = self.esci).grid(
      column = 0, row = 0, sticky = 'e')

      Button(width = 10, text = "Differenza", command = self.diff).grid(
      column = 0, row = 3, sticky = 'n')

      Button(width = 10, text = "Prodotto", command = self.molt).grid(
      column = 0, row = 4, sticky = 'n')

      Button(width = 10, text = "Quoziente", command = self.div).grid(
      column = 0, row = 5, sticky = 'n')

      Label(width = 10, text = "Risultato").grid(
      column = 0, row = 6, sticky = 'n')

  def start(self):
	  self.mainloop()

  def somma(self):
      self.risultato.set(self.numero.get() + self.numero1.get())

  def diff(self):
      self.risultato.set(self.numero.get() - self.numero1.get())

  def cancella(self):
      self.risultato.set(0)
      self.numero.set(0)
      self.numero1.set(0)

  def esci(self):
      exit(0)

  def molt(self):
      self.risultato.set(self.numero.get() * self.numero1.get())

  def div(self):
      self.risultato.set(self.numero.get() / self.numero1.get())


win = Finestra()
win.start()
