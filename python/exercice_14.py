ch1 = "laval"
ch2 = ""  # chaine inversée
for lettre in ch1:
    ch2 = lettre + ch2  # on ajoute la lettre en premier
if ch2 == ch1:

            print ("il s'agit d'uhn palyndrome")
            exit()
else:
        print(ch2)
        print("il ne s'agit pas d'un  palyndrome")
        exit()