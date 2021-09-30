annee=int(input("Entrer l'annee:"))

if annee%4 == 0 and annee%100 != 0 or annee%400 == 0:
    print("{} est bissextile".format(annee))
else:
    print("{} n'est pas bissextile".format(annee))
