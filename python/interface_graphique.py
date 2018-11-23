
#!/usr/bin/env python
#-*- coding:utf-8-*-
# ----------Fenetre ----------------
from tkinter import*
fenetre=Tk()
label=Label(fenetre,text="Bienvenue dans le calculateur d'imc ! ")

label.pack()
#-----------Boutton Poids

masse= Entry(fenetre, textvariable = value, width=4)
masse.pack(side=LEFT, padx=5, pady=5)
#-----------Boutton Taille

taille= Entry(fenetre, textvariable = value1, width=4)
taille.pack(side=RIGHT, padx=10, pady=5)
#---------Conversion
print(type (taille.get()))
t=float(taille.get())
bouton=Button(fenetre,text="calculez votre imc",command=imc(p,t))
bouton.pack()
fenetre.mainloop()

