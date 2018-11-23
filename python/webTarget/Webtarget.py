# fonction permettant de lire et écrire dans un fichier
def ecrire(Adresslist):
    Adress = open("listeAdress.csv","a")
    Adress.write(Adresslist)
    Adress.write("\n")
    Adress.close()
def lire():
    Adress = open("path", "r")
    print(Adress.read())
    Adress.close()
def doublons():
    f = open('listeAdress.csv')
    li = []
    while 1:
        ln = f.readline().split()
        if ln:
            li.append(ln)
        else:
            break
    f.close()
    return li
car="@"
com=".com"
fr=".fr"
import os
hostname = "googl" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'is up!'
else:
  print hostname, 'is down!'

while True:
    Adresslist=input("veuillez entrer une adresse mail valide:\n")
    if car in Adresslist:
        if com in Adresslist:
            break
        elif fr in Adresslist:
            break
    print("adress mail incorrect !")

ecrire(Adresslist)
print("vous avez rentrer 1 adresse:\n")
liste=[]
liste=doublons()


print(liste)

