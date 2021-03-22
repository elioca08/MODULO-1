import sqlite3
from  wordsdata import Words

conn = sqlite3.connect('words.db')
c = conn.cursor()

#c.execute(""" CREATE TABLE words (
#    palabra  text,
#    significado text
#    )""")

def insertar_words(w):
   with conn:
    c.execute("INSERT INTO words VALUES (:palabra,:significado)",{'palabra':w.palabra, 'significado':w.significado})


def cargar_significado(w, definicion):
    with conn:
      c.execute("""UPDATE words SET significado = :significado
      WHERE palabra = :palabra""",
      {'palabra': w, 'significado': definicion})


def buscar_words(w):
  c.execute("SELECT * FROM  words WHERE palabra = :palabra ",{'palabra':w})
  return c.fetchone()


def borrar_palabra(w):
    with conn:
      c.execute("DELETE from words WHERE palabra = :palabra",
      {'palabra':w})


print("Escoger una opción")
print("A.Agregar nueva palabra")
print("B.Editar palabra")
print("C.ELiminar palabra")
print("D.Buscar significado de palabra")
print("E.Mostrar palabras")

opc = str(input("Elegir "))


if opc == 'A':
  p = input("Escribir la palabra que desea añadir ")
  s = input("Escribir el significado de la palabra ")
  w=Words(p,s)
  insertar_words(w)

if opc == 'B':
  p = input("Escribir la palabra que desea editar ")
  s = input("Escribir el nuevo significado de la palabra ")
  cargar_significado(p, s)

if opc == 'C':
  p = input("Escribir la palabra que desea borrar ")
  borrar_palabra(p)

if opc == 'D':
  p = input("Escribir la palabra que desea buscar ")
  w = buscar_words(p)
  print(w)


if opc == 'E':
  c.execute("SELECT palabra, significado FROM  words ")
  w = c.fetchall() 
  for i in w:
   print (i)



conn.close