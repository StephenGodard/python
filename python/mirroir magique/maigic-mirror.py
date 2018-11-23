from tkinter import *
import os
import threading
import time
'''''
fenetre=Tk()

#Creation du widget contenant l'image
photo = PhotoImage(file='Include/Magic_Mirror.png')
photo2 = PhotoImage(file='Include/miroir.png')

canvas1 = Canvas(fenetre, width=1000, height=800)
canvas1.create_image(0, 0, anchor=NW, image=photo)
canvas1.pack()

canvas2 = Canvas(fenetre,width=1000, height=800)
canvas2.create_image(0, 0, anchor=NW, image=photo2)
canvas2.pack()

fenetre.mainloop()
'''''


import threading, time, random, copy
from serial import *
# définition du thread
class MonThread (threading.Thread) :
    def __init__ (self, win, res) :
        threading.Thread.__init__ (self)
        self.win = win  # on mémorise une référence sur la fenêtre
        self.res = res

    def run (self) :
      with Serial(port="/dev/ttyUSB0",baudrate=9600, timeout=1) as port_serie:
          while True :
              ligne=port_serie.readline()
              ligne1=[ligne.decode('utf-8')]
              print(ligne.decode('utf-8'))
              fichier =open("~/PycharmProjects/piscinepython/venv/include/data.txt", "w")
              fichier.write(ligne.decode('utf-8'))
              fichier.close(ligne.decode('utf-8'))

thread_resultat = []

def lance_thread () :
    global thread_resultat
      # fonction appelée lors de la pression du bouton
      # on change la légnde de la zone de texte
      # on désactive le bouton pour éviter de lancer deux threads en même temps
    bouton.config (state = TK.DISABLED)
      # on lance le thread
    m = MonThread (root, thread_resultat)
    m.start ()

def thread_fini_fonction (e) :
    global thread_resultat
      # fonction appelée lorsque le thread est fini
    print("la fenêtre sait que le thread est fini")
      # on change la légende de la zone de texte

      # on réactive le bouton de façon à pouvoir lancer un autre thread
    bouton.config (state = TK.NORMAL)

import tkinter as TK

# on crée la fenêtre
root   = TK.Tk ()
bouton = TK.Button (root, text = "lecture arduino", command = lance_thread)
bouton.pack ()

photo = PhotoImage(file='~/PycharmProjects/piscinepython/venv/include/Magic_mirror.png')
canvas1 = Canvas(root, width=1000, height=800)
canvas1.create_image(0, 0, anchor=NW, image=photo)
canvas1.pack()

# on associe une fonction à un événement <<thread_fini>> propre au programme
root.bind ("<<thread_fini>>", thread_fini_fonction)


# on active la boucle principale de message
root.mainloop ()
