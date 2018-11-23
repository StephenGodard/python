###def imc(p,t):
def imc(p,t):
    t=float(t/100)
    imc=float(p/(t*t))
    print("imc:",imc)
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

from tkinter import *
def correct(v,inp):

    if inp.isdigit():

        return True
    elif inp is "":

        return True

    else:

        return False


def buttonClick():
    float_masse = int(masse.get())
    float_taille = int(taille.get())
    print(float_masse)
    print(float_taille)
    imc(float_masse,float_taille)

fenetre = Tk()
fenetre.configure(width="400",height="200")

masse = Entry(fenetre)
masse.place(x=50,y=50)
labelMasse=Label(fenetre,text="poids en kg:")
labelMasse.place(x=50,y=25)
taille = Entry(fenetre)
taille.place(x=200,y=50)
labelTaille=Label(fenetre,text="taille en cm:")
labelTaille.place(x=200,y=25)
reg=fenetre.register(correct)
masse.config(validate="key",validatecommand=(reg,'%v','%P'))
taille.config(validate="key",validatecommand=(reg,'%v','%P'))
submitButton=Button(fenetre,text="submit",command=buttonClick)
submitButton.place(x=150,y=75)



fenetre.mainloop()
