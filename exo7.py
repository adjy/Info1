annee=int(input("Entrer l'annee:"))
"Une année est bissextile si elle est multiple de 4 sans être multiple de 100 ou si elle est
multiple de 400, si non, elle n'est pas bissextile"

if annee%4 == 0 and annee%100 != 0 or annee%400 == 0:
    print("{} est bissextile".format(annee))
else:
    print("{} n'est pas bissextile".format(annee))
