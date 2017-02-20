from tkinter import *
from mago import Mago
from strega import Strega

class win(Tk):
  def __init__(self):
   Tk.__init__(self)
   self.title("Gioco")
   self.geometry("328x200")
   self.config(bg = "green")

   self.punti = IntVar()
   self.forza = IntVar()
   self.vita = IntVar()    
   self.poteri = IntVar()
   self.magia = IntVar()

   Label(text = "Strega", width = 20).grid(
   column = 0, row = 0, sticky = 'nsew')

   Label(text = "Mago", width = 20).grid(
   column = 1, row = 0, sticky = 'nsew')

   Button(text = "Mostra abilita'", width = 15, command = self.abilita).grid(
   column = 0, row = 1, sticky = 'nsew')   

   Button(text = "Mostra abilita'", width = 15, command = self.abilita_2).grid(
   column = 1, row = 1, sticky = 'nsew') 

  def start(self):
   self.mainloop()

  def abilita(self): 
   m = Mago(self.punti, self.forza)
   self.vita.set(m.stampa_punti())
   self.poteri.set(m.stampa_Forza())

   Label(text = "Punti:", width = 5).grid(
   column = 0, row = 2, sticky = 'w')
   Label(width = 15, textvariable = self.vita).grid(
   column = 0, row = 2, sticky = 'e')
  
   Label(text = "Forza:", width = 5).grid(
   column = 0, row = 3, sticky = 'w')
   Label(width = 15, textvariable = self.poteri).grid(
   column = 0, row = 3, sticky = 'e')

  def abilita_2(self):
   s = Strega(self.punti, self.forza)
   self.vita.set(s.return_punti())
   self.magia.set(s.return_forza())

   Label(text = "Punti:", width = 5).grid(
   column = 1, row = 2, sticky = 'w')
   Label(width = 15, textvariable = self.vita).grid(
   column = 1, row = 2, sticky = 'e')
  
   Label(text = "Forza:", width = 5).grid(
   column = 1, row = 3, sticky = 'w')
   Label(width = 15, textvariable = self.magia).grid(
   column = 1, row = 3, sticky = 'e')

  
finestra = win()
finestra.start()
