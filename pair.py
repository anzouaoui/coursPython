##Ecrire un programme qui test si n nombre est pair ou impair
##Demende de saisie d'un nombre
nombre = int (input("Saisir un nombre: "))

if(nombre%2 == 0):
    print(nombre, " est un nombre pair")
else:
    print(nombre, " est un nombre impair")
