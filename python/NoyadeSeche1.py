def recup_jour(a):
    #fonction qui fait: 30/09/2018 => 30
    day = a[0]
    Dday = a[1]
    day = day + Dday
    return day
#fonction
def recup_mois(a):
    # fonction qui fait: 30/09/2018 => 09
    month=a[3]
    Dmonth=a[4]
    month=month+Dmonth
    return month
def last(a):
    # fonction qui fait: 2018 => 18
    years=a[6]
    Dyears=a[7]
    Cyears=a[8]
    Myears=a[9]
    last=Cyears + Myears
    return last
def add_month(a):
    #on ajoute selon le mois
    if a==1 or a==10:
        return 0
    elif a==5:
        return 1
    elif a==8:
        return 2
    elif a==2 or a==3 or a==11:
        return 3
    elif a==6:
        return 4
    elif a==9 or a==12:
        return 5
    elif a==7 or a==4:
        return 6
def first(a):
    #fonction qui fait:2018 => 20
    years = a[6]
    Dyears = a[7]
    Cyears = a[8]
    Myears = a[9]
    first = years + Dyears
    return first
def years(a):
    # fonction qui fait:30/09/2018 => 2018
    Eyears = a[6]
    Dyears = a[7]
    Cyears = a[8]
    Myears = a[9]
    years=Eyears + Dyears + Cyears + Myears
    return years
def bissextile(a):
    #verif annee bissextile
    if a%4==0:
        print("il s'agit d'une année bissextile")
        return 1

    else:
        print("il ne s'agit pas d'une année bissextile")
        return 0

# Début du code:programme permettant de récupérer le jour le la semaine en fonction de la date
while True:

    #--------Boucle permettant de valider une date correct
    date = input("veuillez entrer la date du jour au format jj/mm/aaaa:\n")
    if date.__len__() != 10:
        print("date incorrect !")
    else:
        print("date correct!")
        break
    #---------On récupère le jours le mois et l'année
day=int(recup_jour(date))
month=int(recup_mois(date))
lastChiffres=int(last(date))
years=int(years(date))
   #Etape 2: On ajoute 1/4 de ce chiffre en ignorant les restes
Etape2=float(lastChiffres/4)
lastChiffres=lastChiffres+Etape2
   #Etape 3:On ajoute la journée du mois
lastChiffres=lastChiffres+day
ajouter_mois=add_month(month)
verifAnnee=bissextile(years)
#on verifie s'il s'agit d'une annee bissextile
if month==1 or month==2 and verifAnnee==1 :
    lastChiffres-=1

lastChiffres=lastChiffres+ajouter_mois
siecle=int(first(date))
#selon le siecle on ajoute S
if siecle==16:
    S=6
elif siecle==17:
    S=4
elif siecle==18:
    S=2
elif siecle==19:
    S=0
elif siecle==20:
    S=6
elif siecle==21:
    S=4

lastChiffres=lastChiffres+S
Dday=int(lastChiffres%7)

#on récupère la date et on affiche
if Dday==1:
    print("nous somme Lundi")
elif Dday==2:
    print("Nous somme Mardi")
elif Dday==3:
    print("Nous somme Mercredi")
elif Dday==4:
    print("Nous somme Jeudi")
elif Dday==5:
    print("Nous somme Vendredi")
elif Dday==6:
    print("Nous somme Samedi")
elif Dday==0:
    print("Nous somme Dimanche")





