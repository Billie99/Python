from gasp import *

begin_graphics() # crea la finestra

Line((100, 100), (200, 200)) # traccia una linea
Circle((320, 240), 40) # traccia una circonferenza
Box((400, 300), 100, 85) # traccia un rettangolo

update_when('key_pressed') # aspetta un tasto quando e' premuto
end_graphics() # chiude la finestra

