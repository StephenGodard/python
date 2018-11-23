liste =[17, 38, 10, 25, 7]
liste.append(12)
liste.sort()
print(liste.index(17))
del liste[5]
print (liste)
for i in range(1,3,1):
    print( liste[i])