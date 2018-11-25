def Add():
    Add=Tk()
    Add.configure(width="200",height="200")
    label=Label(Add,tex="Nouvel adresse:")
    newAdress=Entry(Add)


import tkinter
from tkinter import *
main=Tk()
main.configure(width="680",height="550")
Add=Button(main,text="Ajouter",command=Add())