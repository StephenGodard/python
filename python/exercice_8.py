a = int(input("entrez un nombre  entre 1 et 10!"))
while(1):
    if(a>1 and a<10):
        print("validé ! votre nombre:",a)
        exit()
    else:
     print("nombre non valide veuillez entrer à nouveau un nombre entre 1 et 10")
     a = int(input("entrez un nombre  entre 1 et 10!"))

