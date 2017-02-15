from tkinter import *
from tkinter import ttk

def quit():
          print("L'applicazione e' stata arrestata")
          exit(0)

def doppio():
	     try:
                 risultato.set(float(numero.get()) * 2.0)
	     except:
                    risultato.set("Stringa non valida")
	
win = Tk()
win.title("Calcolatrice")
frame = ttk.Frame(win)

numero = StringVar()
risultato = StringVar()

frame.grid(column = 0, row = 0, sticky = 'nsew')

ttk.Label(frame, width = 15, text = "INSERISCI NUMERO ").grid(
        column = 0, row = 0, sticky = 'w')

Entry(frame, textvariable = numero).grid(column = 2, row = 0, sticky = 'w')
Button(win, text = "Esci", command = quit).grid(
        column = 0, row = 1, sticky = 'nsew')

Button(frame, text = "Doppio", command = doppio).grid(
        column = 0, row = 1, sticky = 'nsew')

ttk.Label(frame, width = 15, textvariable = risultato).grid(
	column = 2, row = 1, sticky = 'e')

win.mainloop()


