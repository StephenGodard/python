#!/usr/bin/env python
#-*- coding:utf-8-*-

def Add():
    newWindow = Toplevel()

    newWindow.focus_set()
    newWindow.geometry("300x250")

    newWindow.title("Ajouter")
    label=Label(newWindow,text="Ajouter une adresse mail:")
    label.place(x=75,y=50)
    global newAdress
    newAdress = Entry(newWindow, width=30, justify='right')
    newAdress.place(x=75,y=75)
    car = "@"
    com = ".com"
    fr = ".fr"

    buttonPrint = Button(newWindow, text="ok",command=Ajouter)

    buttonPrint.place(x=75,y=105)


    print("adress mail incorrect !")
def Ajouter():
    car = "@"
    com = ".com"
    fr = ".fr"
    Adresslist=newAdress.get()
    if car in Adresslist:
        if com in Adresslist:
            Adress = open("listeAdress.csv", "a")
            Adress.write(Adresslist)
            Adress.write("\n")
            Adress.close()
            print("Ajouter !")

        elif fr in Adresslist:
            Adress = open("listeAdress.csv", "a")
            Adress.write(Adresslist)
            Adress.write("\n")
            Adress.close()
            print("Ajouter !")
    print("adress mail incorrect !")
def double():
    with open("listeAdress.csv") as Adresslist:

        line=[]
        cnt=0
        line_str=Adresslist.readline()
        line.append(line_str)

        while line:

            cnt += 1
            line_str = Adresslist.readline()
            line.append(line_str)
            print(line[cnt])
            if line[cnt]==line[cnt-1]:
                print(line[cnt])
                print(line_str)
import tkinter
from tkinter import *


main=Tk()
main.configure(width="680",height="550")
Add=Button(main,text="Ajouter",command=Add)
Add.place(x=150,y=75)
#csv=Button(main,text="import csv",command=csv)
#csv.place(x=300,y=75)
double=Button(main,text="Dédoubloner",command=double)
double.place(x=150,y=150)
main.mainloop()
