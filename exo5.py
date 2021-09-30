'''
premier_nombre = int(input("Entrer le premier nombre:"))
deuxieme_nombre = int(input("Entrer le dexieme nombre:"))

if premier_nombre * deuxieme_nombre <0:
    print("Le produit est negatif")
elif  premier_nombre * deuxieme_nombre ==0:
    print("Le produit est nul")
else:
    print("Le produit est positif")
'''

premier_nombre = int(input("Entrer le premier nombre:"))
deuxieme_nombre = int(input("Entrer le dexieme nombre:"))

if premier_nombre <0 or deuxieme_nombre <0:
    print("Le produit est negatif")
elif  premier_nombre == 0 or deuxieme_nombre ==0:
    print("Le produit est nul")
else:
    print("Le produit est positif")
