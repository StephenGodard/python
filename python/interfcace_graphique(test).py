#!/usr/bin/env python
#-*- coding:utf-8-*-

from tkinter import*
fenetre=Tk()
label=Label(fenetre,text="hello world")
label.pack()
fenetre.mainloop()

###def imc(p,t):
def imc(p,t):
    imc=p/(t*t)
    if imc<16:
        print("anorexie contactez au plus vite votre médecin")
    elif imc>16 and imc<18.5:
        print("maigreur")
    elif imc>18.5 and imc<25:
        print("Corpulence normale")
    elif imc>25 and imc<30:
        print("surpoids")
    elif imc>30 and imc<35:
        print("Obésité modéré(Classe 1")
    elif imc>35 and imc> 40:
                print("obésité modérer(classe 2")
    else:
        print("obésité morbide contactez au plus vite votre médecin")
    return imc
