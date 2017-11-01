##Creer 2 collections de mails

##Importation de la librairie re
import re
##importation de la librarie collection
import collections

##Définition de la fonction permettant d'afficher une liste
def affiche(liste):
    for item in liste:
        print("  ", item)

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

##Verification de la validité des mails
validMail = []
invalidMail = []
for mail in whiteList1:
    if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail) != None):
       validMail.append(mail)
    else:
       invalidMail.append(mail)
print("Mails valides: ")
affiche(validMail)
print("\nMails invalides: ")
affiche(invalidMail)
print("\nDoublons: ")
doublon(whiteList1)
print("\nEnsemble de whiteliste1 et de whiteliste2: ")
afficherTout(whiteList1, whiteList2)


