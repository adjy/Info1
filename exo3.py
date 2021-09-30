'''
a = int(input("ENter la 1ere valeur:"))
b = int(input("ENter la 2eme valeur:"))
c = int(input("ENter la 3eme valeur:"))
d = int(input("ENter la 4eme valeur:"))
e = int(input("ENter la 5eme valeur:"))

somme=a+b+c+d+e

print("La somme est:", somme)
'''
i=1
somme=0
while i<=5:
    entrer = int(input("Entrer la {} valeur: ".format(i)))
    somme= somme+entrer
    i+=1

print("La somme est:", somme)