from tkinter import *
from turtle import *
from tkinter.colorchooser import askcolor
from math import sqrt
from triangolo import *
from punto import *
from quadrato import *
from Poligono import *

class Finestra(Tk):
  def __init__(self):

      Tk.__init__(self)

      self.title("Coordinate Poligono")
      self.geometry("564x360")  
      self.config(bg = "green")      

      self.xm = StringVar()
      self.ym = StringVar()
      self.AreaTriangolo = StringVar()
      self.AreaPoligono = StringVar()
      self.PuntoMedio = StringVar()
      self.x = StringVar()
      self.y = StringVar()
      self.x1 = StringVar()
      self.y1 = StringVar()
      self.x2 = StringVar()
      self.y2 = StringVar()
      self.punti = StringVar()
      self.x3 = StringVar()
      self.y3 = StringVar()
      self.x4 = StringVar()
      self.y4 = StringVar()
      self.x5 = StringVar()
      self.y5 = StringVar()
      self.x6 = StringVar()
      self.y6 = StringVar()
      self.x7 = StringVar()
      self.y7 = StringVar()
      self.x8 = StringVar()
      self.y8 = StringVar()
      self.x9 = StringVar()
      self.y9 = StringVar()
      self.somma = StringVar()

      Label(text = "Quanti punti vuoi?", width = 25).grid(
      column = 0, row = 0 , sticky = 'nsew')
      Entry(width = 20, textvariable = self.punti).grid(
      column = 1, row = 0, sticky = 'nsew')
      Button(text = "Mostra Punti", width = 21, command = self.Input).grid(
      column = 2, row = 0, sticky = 'nsew')      


  def Input(self):

      Label(text = "Triangolo", width = 20).grid(
      column = 1, row = 0, sticky = 'nsew')
      Label(text = "Punti", width = 20).grid(
      column = 0, row = 0, sticky = 'nsew')
      Label(text = "Inserisci x", width = 20).grid(
      column = 1, row = 0, sticky = 'nsew')
      Label(text = "Inserisci y", width = 20).grid(
      column = 2, row = 0, sticky = 'nsew')


      

      Label(text = "A", width = 20).grid(
      column = 0, row = 1, sticky = 'nsew')
      Label(text = "B", width = 20).grid(
      column = 0, row = 2, sticky = 'nsew')
      Label(text = "C", width = 20).grid(
      column = 0, row = 3, sticky = 'nsew')
      Label(width = 20, textvariable = self.AreaPoligono).grid(
      column = 1, row = 12, sticky = 'nsew')
      Label(text = "D", width = 20).grid(
      column = 0, row = 4, sticky = 'nsew')
      Label(text = "E", width = 20).grid(
      column = 0, row = 5, sticky = 'nsew')
      Label(text = "F", width = 20).grid(
      column = 0, row = 6, sticky = 'nsew')
      Label(text = "G", width = 20).grid(
      column = 0, row = 7, sticky = 'nsew')
      Label(text = "H", width = 20).grid(
      column = 0, row = 8, sticky = 'nsew')
      Label(text = "I", width = 20).grid(
      column = 0, row = 9, sticky = 'nsew')
      Label(text = "L", width = 20).grid(
      column = 0, row = 10, sticky = 'nsew')
      Label(width = 20, textvariable = self.PuntoMedio).grid(
      column = 1, row = 13, sticky = 'nsew')
      Label(width = 20, textvariable = self.AreaTriangolo).grid(
      column = 1, row = 14, sticky = 'nsew')




      Entry(width = 10, textvariable = self.x).grid(
      column = 1, row = 1, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y).grid(
      column = 2, row = 1, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x1).grid(
      column = 1, row = 2, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y1).grid(
      column = 2, row = 2, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x2).grid(
      column = 1, row = 3, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y2).grid(
      column = 2, row = 3, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x3).grid(
      column = 1, row = 4, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y3).grid(
      column = 2, row = 4, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x4).grid(
      column = 1, row = 5, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y4).grid(
      column = 2, row = 5, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x5).grid(
      column = 1, row = 6, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y5).grid(
      column = 2, row = 6, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x6).grid(
      column = 1, row = 7, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y6).grid(
      column = 2, row = 7, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x7).grid(
      column = 1, row = 8, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y7).grid(
      column = 2, row = 8, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x8).grid(
      column = 1, row = 9, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y8).grid(
      column = 2, row = 9, sticky = 'nsew')
      Entry(width = 10, textvariable = self.x9).grid(
      column = 1, row = 10, sticky = 'nsew')
      Entry(width = 10, textvariable = self.y9).grid(
      column = 2, row = 10, sticky = 'nsew')




      Button(text = "Area di un Triangolo", width = 20, command = self.Area_con_medio).grid(
      column = 2, row = 13, sticky = 'nsew')
      Button(text = "Punto Medio", width = 20, command = self.Punto_medio).grid(
      column = 0, row = 13, sticky = 'nsew')
      Button(text = "Mostra figura", width = 20, command = self.Calcoli).grid(
      column = 0, row = 11, sticky = 'nsew')
      Button(text = "Reset", width = 20, command = self.Reset).grid(
      column = 1, row = 11, sticky = 'nsew')
      Button(text = "Esci", width = 20, command = self.Esci).grid(
      column = 2, row = 11, sticky = 'nsew')
      Button(text = "Cambia colore", width = 20, command = self.Color).grid(
      column = 2, row = 12, sticky = 'nsew')
      Button(text = "Area", width = 20, command = self.Area).grid(
      column = 0, row = 12, sticky = 'nsew')



  def Calcoli(self):
      tess = Screen()

      tess.setup(700)
      tess.title("Figure Geometriche")
      tess.bgcolor("lightblue")

      alfa = Turtle()

      alfa.pensize(3)
      alfa.speed(1)
      alfa.color("Blue")  

 
      if float(self.punti.get()) == 3:

         alfa.goto(float(self.x.get()), float(self.y.get()))
         alfa.write(str( "(" + " " + "x = " + self.x.get()) + " " + "," + " " + "y = " + str(self.y.get() + " " + ")"))
         alfa.goto(float(self.x1.get()), float(self.y1.get()))
         alfa.write(str( "(" + " " + "x = " + self.x1.get()) + " " + "," + " " + "y = " + str(self.y1.get() + " " + ")"))
         alfa.goto(float(self.x2.get()), float(self.y2.get()))
         alfa.write(str( "(" + " " + "x = " + self.x2.get()) + " " + "," + " " + "y = " + str(self.y2.get() + " " + ")"))


      elif float(self.punti.get()) == 4:
            
           alfa.goto(float(self.x.get()), float(self.y.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x.get()) + " " + "," + " " + "y = " + str(self.y.get() + " " + ")"))
           alfa.color("blue")
           alfa.goto(float(self.x1.get()), float(self.y1.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x1.get()) + " " + "," + " " + "y = " + str(self.y1.get() + " " + ")"))
           alfa.color("blue")
           alfa.goto(float(self.x2.get()), float(self.y2.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x2.get()) + " " + "," + " " + "y = " + str(self.y2.get() + " " + ")"))
           alfa.color("blue")
           alfa.goto(float(self.x3.get()), float(self.y3.get()))
           alfa.color("red")

           alfa.write(str( "(" + " " + "x = " + self.x3.get()) + " " + "," + " " + "y = " + str(self.y3.get() + " " + ")"))
           alfa.color("blue")

           self.xm = (float(self.x.get()) + float(self.x1.get()) + float(self.x2.get()) + float(self.x3.get())) / 4.0
           self.ym = (float(self.y.get()) + float(self.y1.get()) + float(self.y2.get()) + float(self.y3.get())) / 4.0
           alfa.setposition(60, 60)
           alfa.write(str( "(" + " " + "x = " + str(self.xm) + " " + "," + " " + "y = " + str(self.ym) + " " + ")"))

           alfa.goto(self.xm, self.ym)
           alfa.left(135)
           alfa.forward(80)
           alfa.goto(self.xm, self.ym)
           alfa.left(180)
           alfa.forward(80)
           alfa.goto(self.xm, self.ym)
           alfa.right(270)
           alfa.forward(80)
           alfa.goto(self.xm, self.ym)


      elif float(self.punti.get()) == 5:

           alfa.goto(float(self.x.get()), float(self.y.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x.get()) + " " + "," + " " + "y = " + str(self.y.get() + " " + ")"))
           alfa.color("blue")
           alfa.goto(float(self.x1.get()), float(self.y1.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x1.get()) + " " + "," + " " + "y = " + str(self.y1.get() + " " + ")"))
           alfa.color("blue")
           alfa.goto(float(self.x2.get()), float(self.y2.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x2.get()) + " " + "," + " " + "y = " + str(self.y2.get() + " " + ")"))
           alfa.color("blue")
           alfa.goto(float(self.x3.get()), float(self.y3.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x3.get()) + " " + "," + " " + "y = " + str(self.y3.get() + " " + ")"))
           alfa.color("blue")
           alfa.goto(float(self.x4.get()), float(self.y4.get()))
           alfa.color("red")
           alfa.write(str( "(" + " " + "x = " + self.x4.get()) + " " + "," + " " + "y = " + str(self.y4.get() + " " + ")"))
           alfa.color("blue")


           self.xm = (float(self.x.get()) + float(self.x1.get()) + float(self.x2.get()) + float(self.x3.get()) + float(self.x4.get())) / 5.0
           self.ym = (float(self.y.get()) + float(self.y1.get()) + float(self.y2.get()) + float(self.y3.get()) + float(self.y4.get())) / 5.0

           alfa.setposition(self.xm, self.ym)

           alfa.write(str( "(" + " " + "x = " + str(self.xm) + " " + "," + " " + "y = " + str(self.ym) + " " + ")"))

           alfa.goto(self.xm, self.ym)
           alfa.left(168)
           alfa.forward(75)
       
           alfa.goto(self.xm, self.ym)
           alfa.left(142)
           alfa.forward(63)
           alfa.goto(self.xm, self.ym)
           alfa.right(220)
           alfa.forward(66)
           alfa.goto(self.xm, self.ym)
           alfa.left(282)
           alfa.forward(75)
           alfa.goto(self.xm, self.ym)

  def Area(self):

      if float(self.punti.get()) == 4:

         xm = self.xm = (float(self.x.get()) + float(self.x1.get()) + float(self.x2.get()) + float(self.x3.get())) / 4.0
         ym = self.ym = (float(self.y.get()) + float(self.y1.get()) + float(self.y2.get()) + float(self.y3.get())) / 4.0

         x1 = float(self.x.get())
         y1 = float(self.y.get())
         x2 = float(self.x1.get())
         y2 = float(self.y1.get()) 
         x3 = float(self.x2.get())
         y3 = float(self.y2.get())
         x4 = float(self.x3.get())
         y4 = float(self.y3.get())

         p1 = Punto(x1, y1)
         p2 = Punto(x2, y2)
         p3 = Punto(x3, y3)
         p4 = Punto(x4, y4)
         pM = Punto(xm, ym)

         poligono = Poligono([p1, p2, p3, p4, p1], pM)

         self.AreaPoligono.set(poligono.Area()) 

      elif float(self.punti.get()) == 3:

           x1 = float(self.x.get())
           y1 = float(self.y.get())
           x2 = float(self.x1.get())
           y2 = float(self.y1.get())
           x3 = float(self.x2.get())
           y3 = float(self.y2.get())

           p1 = Punto(x1, y1)
           p2 = Punto(x2, y2)
           p3 = Punto(x3, y3)

           triangolo = Triangolo(p1, p2, p3)

           self.AreaPoligono.set(str(triangolo.Area())) 

      elif float(self.punti.get()) == 5:

           xm = self.xm = (float(self.x.get()) + float(self.x1.get()) + float(self.x2.get()) + float(self.x3.get()) + float(self.x4.get()) / 5.0)
           ym = self.ym = (float(self.y.get()) + float(self.y1.get()) + float(self.y2.get()) + float(self.y3.get()) + float(self.y4.get()) / 5.0)

           x1 = float(self.x.get())
           y1 = float(self.y.get())
           x2 = float(self.x1.get())
           y2 = float(self.y1.get())
           x3 = float(self.x2.get())
           y3 = float(self.y2.get())
           x4 = float(self.x3.get())
           y4 = float(self.y3.get())
           x5 = float(self.x4.get())
           y5 = float(self.y4.get())

           p1 = Punto(x1, y1)
           p2 = Punto(x2, y2)
           p3 = Punto(x3, y3)
           p4 = Punto(x4, y4)
           p5 = Punto(x5, y5)
           pM = Punto(xm, ym)

           poligono = Poligono([p1, p2, p3, p4, p5, p1], pM)

           self.AreaPoligono.set(str(poligono.Area()))

  def Area_con_medio(self):

      if float(self.punti.get()) == 4:

           xm = self.xm = (float(self.x.get()) + float(self.x1.get()) + float(self.x2.get()) + float(self.x3.get())) / 4.0
           ym = self.ym = (float(self.y.get()) + float(self.y1.get()) + float(self.y2.get()) + float(self.y3.get())) / 4.0

           x1 = float(self.x.get())
           y1 = float(self.y.get())
           x2 = float(self.x1.get())
           y2 = float(self.y1.get())

           p1 = Punto(x1, y1)
           p2 = Punto(x2, y2)
           p3 = Punto(xm, ym)

           triangolo = Triangolo(p1, p2, p3)

           self.AreaTriangolo.set(float(triangolo.Area()))

      elif float(self.punti.get()) == 5:

           xm = self.xm = (float(self.x.get()) + float(self.x1.get()) + float(self.x2.get()) + float(self.x3.get()) + float(self.x4.get()) / 5.0)
           ym = self.ym = (float(self.y.get()) + float(self.y1.get()) + float(self.y2.get()) + float(self.y3.get()) + float(self.y4.get()) / 5.0)

           x1 = float(self.x.get())
           y1 = float(self.y.get())
           x2 = float(self.x1.get())
           y2 = float(self.y1.get())
           x4 = float(self.x2.get())
           y4 = float(self.y2.get())
           x5 = float(self.x3.get())
           y5 = float(self.y3.get())

           p1 = Punto(x1, y2)
           p2 = Punto(x2, y2)
           p3 = Punto(xm, ym)

           triangolo = Triangolo(p1, p2, p3)

           self.AreaTriangolo.set(float(triangolo.Area()))

  def Color(self):

      color = askcolor()
      self.config(bg = color[1])      

  def Punto_medio(self):
      
      if float(self.punti.get()) == 3:
         
         x1 = float(self.x.get())
         y1 = float(self.y.get())
         x2 = float(self.x1.get())
         y2 = float(self.y1.get())
         x3 = float(self.x2.get())
         y3 = float(self.y2.get())

         p1 = Punto(x1, y1)
         p2 = Punto(x2, y2)
         p3 = Punto(x3, y3)

         self.PuntoMedio.set(Punto.medio([p1, p2, p3]))

      elif float(self.punti.get()) == 4:

           x1 = float(self.x.get())
           y1 = float(self.y.get())
           x2 = float(self.x1.get())
           y2 = float(self.y1.get())
           x3 = float(self.x2.get())
           y3 = float(self.y2.get())
           x4 = float(self.x3.get())
           y4 = float(self.y3.get())

           p1 = Punto(x1, y1)
           p2 = Punto(x2, y2)
           p3 = Punto(x3, y3)
           p4 = Punto(x4, y4)

           self.PuntoMedio.set(Punto.medio([p1, p2, p3, p4]))

      elif float(self.punti.get()) == 5:

           x1 = float(self.x.get())
           y1 = float(self.y.get())
           x2 = float(self.x1.get())
           y2 = float(self.y1.get())
           x3 = float(self.x2.get())
           y3 = float(self.y2.get())
           x4 = float(self.x3.get())
           y4 = float(self.y3.get())
           x5 = float(self.x4.get())
           y5 = float(self.y4.get())
           
           p1 = Punto(x1, y1)
           p2 = Punto(x2, y2)
           p3 = Punto(x3, y2)
           p4 = Punto(x4, y4)
           p5 = Punto(x5, y5)
           
           self.PuntoMedio.set(Punto.medio([p1, p2, p3, p4, p5]))

      else:
           exit(0)

  def Reset(self):

      self.x.set("")
      self.x1.set("")
      self.x2.set("")
      self.y.set("")
      self.y1.set("")
      self.y2.set("")
      self.AreaTriangolo.set("")
      self.AreaPoligono.set("")
      self.x3.set("")
      self.y3.set("")
      self.x4.set("")
      self.x5.set("")
      self.y4.set("")
      self.y5.set("")
      self.x6.set("")
      self.y6.set("")
      self.x7.set("")
      self.x8.set("")
      self.y7.set("")
      self.y8.set("")
      self.x9.set("")
      self.y9.set("")
      self.PuntoMedio.set("")

  def Esci(self):
      exit(0)

  def start(self):
      self.mainloop()


win = Finestra()
win.start()

