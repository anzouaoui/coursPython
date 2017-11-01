##Exporter et importer dans un csv
##importation de la librarie collection
import collections
##importation de la librairie svg
import csv

##Définition de la fonction permettant d'afficher une liste
def affiche(liste):
    for item in liste:
        print("  ", item)

##Ecrire dans un fichier CSV
def exportCVS(liste, nomFichier):
    nomFichier += ".csv"
    with open(nomFichier, 'w') as csvfile:
        wrCSV = csv.writer(csvfile, delimiter = ";",quoting=csv.QUOTE_ALL)
        wrCSV.writerow(liste);

##Ecrire dans un fichier TXT
def exportTXT(liste, nomFichier):
    nomFichier += ".txt"
    txtFile = open(nomFichier, 'w')
    for item in liste:
        txtFile.write(item + "\n")
    txtFile.close()
    
##Définition de la fonction permttant de détecter les doublons
def doublon(liste):
    whiteList1_doublon = [mail for mail, count in collections.Counter(liste).items() if count > 1]
    affiche(whiteList1_doublon)

##Définition de la fonction permettant d'afficher deux listes
def afficherTout(liste1, liste2):
    listeTotal = liste1[:] + liste2[:]
    affiche(listeTotal)

whiteList1 = ["martin.duouit@gmail.com", "Jdoe@gmail.com", "PaulDupuis@gmail.com", "charlotte.blanc@mail.fr", "martin.duouit@gmail.com", "claire.duval.com", "ahmed.zouaoui@mail.fr", "PaulDupuis@gmail.com"]
whiteList2 = ["test@test.com", "ahmed.zouaoui@mail.fr", "mail@gmail.com", "mail.mail.fr", "blanche@free.fr", "anouk.zouaoui@gmail.com", "martin.duouit@gmail.com"]
blackList = ["test@test.com", "martin.duouit@gmail.com", "mail.mail.fr"]

##menu
print("======== MENU ========")
print("1- Afficher la première liste\n2- Afficher la deuxième liste\n3- Afficher les doulons de la première liste\n4- Afficher la Blacklist\n5- Afifcher l'ensemble des listes\n6- Importer un fichier CSV")
choix = input("\n Que choisissez vous? ")

if choix == '1':
    print("Première liste: ")
    affiche(whiteList1)
    print("\nVoulez-vous sauveagrder en\n   1- CSV\n   2- TEXTE")
    choix2 = input("Veuillez choisir: ")
    if choix2 == '1':
        exportCSV(whiteList1, 'première liste')
    elif choix2 == '2':
        exportTXT(whiteList1, 'première liste')
        
elif choix == '2':
    print("Deuxième liste: ")
    affiche(whiteList2)
    print("\nVoulez-vous sauveagrder en\n   1- CSV\n   2- TEXTE")
    choix2 = input("Veuillez choisir: ")
    if choix2 == '1':
        exportCSV(whiteList1, 'deuxième liste')
    elif choix2 == '2':
        exportTXT(whiteList1, 'deuxième liste')
elif choix == '3':
    print("Doublons de la première liste: ")
    doublon(whiteList1)
    print("\nVoulez-vous sauveagrder en\n   1- CSV\n   2- TEXTE")
    choix2 = input("Veuillez choisir: ")
    if choix2 == '1':
        exportCSV(whiteList1, 'liste des doublons')
    elif choix2 == '2':
        exportTXT(whiteList1, 'liste des doublons')
elif choix == '4':
    print("Blacklist: ")
    affiche(blackList)
    print("\nVoulez-vous sauveagrder en\n   1- CSV\n   2- TEXTE")
    choix2 = input("Veuillez choisir: ")
    if choix2 == '1':
        exportCSV(whiteList1, 'liste noire')
    elif choix2 == '2':
        exportTXT(whiteList1, 'liste noire')
elif choix == '5':
    print("liste totale des mails")
    afficherTout(whiteList1, whiteList2)
    print("\nVoulez-vous sauveagrder en\n   1- CSV\n   2- TEXTE")
    choix2 = input("Veuillez choisir: ")
    if choix2 == '1':
        exportCSV(whiteList1, 'ensemble')
    elif choix2 == '2':
        exportTXT(whiteList1, 'ensemble')
elif choix == '6':
    print('Saisir le nom du fichier SVG que vous voulez importer: ')
    
