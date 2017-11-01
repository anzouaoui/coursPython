## Mise en place d'une interface d'enregistrement de mail
## On importe Tkinter
from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox as tkMessagebox
import tkinter.simpledialog as tkSimpleDialog

## On importe colections
import collections
## On importe csv
import csv
## On importe re
import re

## Définition des listes
whiteList1 = ["martin.duouit@gmail.com", "Jdoe@gmail.com", "PaulDupuis@gmail.com", "charlotte.blanc@mail.fr", "martin.duouit@gmail.com", "claire.duval.com", "ahmed.zouaoui@mail.fr", "PaulDupuis@gmail.com"]
whiteList2 = ["test@test.com", "ahmed.zouaoui@mail.fr", "mail@gmail.com", "mail.mail.fr", "test@test.com", "blanche@free.fr", "anouk.zouaoui@gmail.com", "martin.duouit@gmail.com", "blanche@free.fr"]
blackList = ["test@test.com", "martin.duouit@gmail.com", "mail.mail.fr"]

## Fonction permettant d'afficher une liste
def affiche(liste):
    for item in liste:
        print(item)
        
## Fonction permettant d'afficher les doublons
def afficheDoublons(liste):
    doublon = [mail for mail, count in collections.Counter(whiteList1).items() if count > 1]
    for item in doublon:
        print(item)

## Exportation en CSV
def exportCSV(liste, nomFichier):
    nomFichier +=  ".csv"
    with open(nomFichier, 'w') as csvfile:
        try:
            wrCSV = csv.writer(csvfile, delimiter = ";",quoting=csv.QUOTE_ALL)
            wrCSV.writerow(liste);
            tkMessagebox.showinfo("Sauvegarde en CSV","Sauvegarde en CSV effectuée")
        except:
            tkMessagebox.showerror("Erreur de sauvegarde","Il y a une erreur lors de la sauvegarde")
    csvfile.close()

## Exportation en texte
def exportTXT(liste, nomFichier):
    nomFichier += ".txt"
    txtFile = open(nomFichier, 'w')
    try:
        for item in liste:
            txtFile.write(item + "\n")
        tkMessagebox.showinfo("Sauvegarde en texte","Sauvegarde en texte effectuée")
    except:
        tkMessagebox.showerror("Erreur de sauvegarde","Il y a une erreur lors de la sauvegarde")
    txtFile.close()

## Ajouter un email
def ajouter(liste):
    valid = False
    while valid == False:
        email = tkSimpleDialog.askstring("Nouvel email", "Saisir l'email que vous voulez ajouter")
        if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None):
            liste.append(email)
            valid = True
        else:
           tkMessagebox.showerror("Erreur de saisie","L'email n'est pas valide")
           print("erreur")

## Modifier un email
def modifier(listbox, liste):
    index = listbox.curselection()
    ## Verification qu'index n'est pas vide
    if index:
        selectionEmail = listbox.get(index[0])
        email = tkSimpleDialog.askstring("Nouvel email", "Saisir l'email que vous voulez modifier")
        selectionEmail.set(email)
        print(selectionEmail)
    else:
        print("erreur")
    
## Fonction permettant d'afficher la permière liste
def afficheWhiteList1():
    fenetrePremiereListe = Tk()
    fenetrePremiereListe.geometry("500x500")
    fenetrePremiereListe.resizable(False, False)
    
    ## Titre de label fenetre
    fenetrePremiereListe.title("Première list")
    
    ## Initialisation d'une liste
    listBoxWhiteList1 = Listbox(fenetrePremiereListe, width=40, height=50)
    listBoxWhiteList1.pack(side=LEFT)
    
    ## Remplissage de la liste
    for item in whiteList1:
        listBoxWhiteList1.insert(END, item)

    ## Création des boutons
    boutonExportCsv = Button(fenetrePremiereListe, text = 'Exporter en CSV', width=30,  command = lambda: exportCSV(whiteList1, 'première liste'))
    boutonExportCsv['font'] = fontButton

    boutonExportCsv.pack(pady=5, side=TOP)

    boutonExportText = Button(fenetrePremiereListe, text = 'Exporter en texte', width=30,  command = lambda: exportTXT(whiteList1, 'première liste'))
    boutonExportText['font'] = fontButton

    boutonExportText.pack(pady=5, side=TOP)

    boutonAjouter = Button(fenetrePremiereListe, text = 'Ajouter un email', width=30, command = lambda: ajouter(whiteList1))
    boutonAjouter['font'] = fontButton

    boutonAjouter.pack(pady=5, side=TOP)

    boutonModifier = Button(fenetrePremiereListe, text = 'Modifier l\'email', width=30, command = lambda: modifier(listBoxWhiteList1, whiteList1))
    boutonModifier['font'] = fontButton

    boutonModifier.pack(pady=5, side=TOP)

    boutonSupprimer = Button(fenetrePremiereListe, text = 'Afficher les doublons\nde la permière liste', width=30)
    boutonSupprimer['font'] = fontButton

    boutonSupprimer.pack(pady=5, side=TOP)
    
    fenetrePremiereListe.mainloop()
    
## Initialisation de la fenetre
fenetre = Tk()
fenetre.geometry("350x500")
fenetre.resizable(False, False)

## Initialisation des polices
fontLabel = tkFont.Font(family='Helvetica', size=18, weight='bold')
fontButton = tkFont.Font(family='Helvetica', size=14)
## Titre de label fenetre
fenetre.title("Gestion des mails")

## Mise en place du menu
mainMenu = Menu(fenetre)
menu = Menu(mainMenu)
menu.add_command(label="Quitter", command = fenetre.destroy)

mainMenu.add_cascade(label = "Fichier", menu = menu)
fenetre.config(menu = mainMenu) 
## Ouverture de l'image
photo = PhotoImage(file="itescia.png")

##Affichage du logo
Largeur = 350
Hauteur = 140
Canevas = Canvas(fenetre,width = Largeur, height =Hauteur, background = "white")
item = Canevas.create_image(0,0,anchor=NW, image=photo)
print("Logo")
Canevas.pack()

## Label du choix
label = Label(fenetre, text="Que souhaitez-vous faire? ")
label.configure(font=fontLabel)
label.pack()

# Création des boutons
boutonPremiereListe = Button(fenetre, text = 'Afficher la première liste', width=30,  command = afficheWhiteList1)
boutonPremiereListe['font'] = fontButton

boutonPremiereListe.pack(pady=5)

boutonDeuxiemeListe = Button(fenetre, text = 'Afficher la deuxième liste', width=30)
boutonDeuxiemeListe['font'] = fontButton

boutonDeuxiemeListe.pack(pady=5)

boutonDoublonsListe1 = Button(fenetre, text = 'Afficher les doublons\nde la permière liste')
boutonDoublonsListe1['font'] = fontButton

boutonDoublonsListe1.pack(pady=5)

boutonDoublonsListe2 = Button(fenetre, text = 'Afficher les doublons\nde la deuxième liste')
boutonDoublonsListe2['font'] = fontButton

boutonDoublonsListe2.pack(pady=5)

boutonBlackList = Button(fenetre, text = 'Afficher la liste noire', width=30)
boutonBlackList['font'] = fontButton

boutonBlackList.pack(pady=5)
fenetre.mainloop()
