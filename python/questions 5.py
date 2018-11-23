pSeuil=2.3
vSeuil=7.41
pSeuilcourant=float(input("saisir la pression courante"))
vSeuilcourant=float(input("saisir le courant courant"))
if pSeuilcourant>pSeuil and vSeuilcourant>vSeuil:
        print("arrêt immédiat")
        exit()
elif pSeuilcourant>pSeuil:
    print ("augmenter le volume de l'enceinte")
    exit()
elif  vSeuilcourant>vSeuil:
        print("diminuer le volume de l'enceinte")
        exit()
else:
         print("tout va bien")
exit()

