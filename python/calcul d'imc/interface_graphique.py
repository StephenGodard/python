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
#!/usr/bin/env python
#-*- coding:utf-8-*-
# ----------Fenetre ----------------
from decimal import Decimal
from tkinter import*
fenetre=Tk()
label=Label(fenetre,text="Bienvenue dans le calculateur d'imc ! ")

label.pack()
#-----------Boutton Poids
value = StringVar()
value.set("")
masse= Entry(fenetre, textvariable = value, width=4)
masse.pack(side=LEFT, padx=5, pady=5)
#-----------Boutton Taille
value1 = StringVar()
value1.set("")
taille= Entry(fenetre, textvariable = value1, width=4)
taille.pack(side=RIGHT, padx=10, pady=5)

#---------Conversion
t=format(masse, '.15g')
m= format(masse, '.15g')
bouton=Button(fenetre,text="calculez votre imc",command=imc(m, t))
bouton.pack()
fenetre.mainloop()

