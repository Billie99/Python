from tkinter import *
from tkinter import ttk
from math import sqrt
from punto import Punto

class finestra(Tk):
  def __init__(self):
      Tk.__init__(self)
      self.title("Calcolatrice")
      self.geometry("300x200")      
      self.config(bg = "blue")

      self.x = IntVar()
      self.y = IntVar()
      self.risultato = IntVar()
      self.num = IntVar()
      self.mun1 = IntVar()  

      Label(text = "Inserisci x", width = 15).grid(
      column = 0, row = 0, sticky = 'nsew')
      Entry(textvariable = self.x, width = 15).grid(column = 0,
      row = 1, sticky = 'nsew')

      Label(text = "Inserisci y", width = 15).grid(
      column = 1, row = 0, sticky = 'nsew')
      Entry(textvariable = self.y, width = 15).grid(column = 1,
      row = 1, sticky = 'nsew')

      Button(text = "Radice Quadrata", width = 15, command = self.distanza).grid(column = 0,
      row = 2, sticky = 'nsew')      
      Label(width = 15, textvariable = self.risultato).grid(
      column = 1, row = 2, sticky = 'nsew')

      Button(width = 15, text = "Cancella", command = self.cancella).grid(
      column = 0, row = 3, sticky = 'nsew') 

      Button(width = 15, text = "Esci", command = self.esci).grid(
      column = 1, row = 3, sticky = 'nsew')

  def start(self):
      self.mainloop()

  def distanza(self):
      p = Punto(self.x.get(), self.y.get())
      self.risultato.set(p.distanza())
 
  def cancella(self):
      self.numero.set(0)
      self.risultato.set(0)

  def esci(self):
      exit(0) 

win = finestra()
win.start()
