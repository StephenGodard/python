# fonction permettant de lire et écrire dans un fichier
def ecrire(Adresslist):
    Adress = open("listeAdress.csv","a")
    Adress.write(Adresslist)
    Adress.write("\n")
    Adress.close()
def lire():
    Adress = open("listeAdress.csv", "r")
    print(Adress.read())
    Adress.close()

def doublons(Adresslist):
    Adress = open("listeAdress.csv", "r")
    for ligne in Adress:
          if Adresslist in ligne:
              Adress.close()
              return True
    else:
        Adress.close()
        return False
import os
compteur = 1
car="@"
com=".com"
fr=".fr"



while True:
    Adresslist=input("veuillez entrer une adresse mail valide:\n")
    if car in Adresslist:
        if com in Adresslist:
            twice=doublons(Adresslist)
            if twice==True:
                print("Adresse déjà sauvegarder")
            else:
                print("adresse correct !")
                break


        elif fr in Adresslist:
            twice = doublons(Adresslist)
            if twice == True:
                print("Adresse déjà sauvegarder")
            else:
                print("adresse correct !")
                break
    print("adress mail incorrect !")


print("vérification du nom de domaine")
domain=Adresslist.split('@')
os.system('ping -c 2'+ ' '+domain[1]+'>pingtest.txt')
if os.path.getsize("pingtest.txt")==0:
    print("KO")
else:
    print("OK")

#print(domain[1])

print("vous avez rentrer 1 adresse:\n ping de l'adresse veuillez patienter...")



