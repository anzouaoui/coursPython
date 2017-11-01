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
## Fonction permettant d'afficher les listes
def afficheListe(liste, nomFichier):
    ## Initialisation d'une fentre d'affichage
    fenetrePremiereListe = Tk()
    fenetrePremiereListe.geometry("500x500")
    fenetrePremiereListe.resizable(False, False)
    ## Titre de label fenetre
    fenetrePremiereListe.title("Première list")
    
    ## Initialisation d'une liste
    listBoxWhiteList1 = Listbox(fenetrePremiereListe, width=40, height=50)
    listBoxWhiteList1.pack(side=LEFT)

    ## Remplissage de la listebox
    remplir(listBoxWhiteList1, liste)

    ## Création des boutons
    ## Bouton permettant d'exporter en CSV
    boutonExportCsv = Button(fenetrePremiereListe, text = 'Exporter en CSV', width=30,  command = lambda: exportCSV(liste, nomFichier))
    boutonExportCsv['font'] = fontButton
    boutonExportCsv.pack(pady=5, side=TOP)

    ## Bouton permettant d'exporter en fichier texte
    boutonExportText = Button(fenetrePremiereListe, text = 'Exporter en texte', width=30,  command = lambda: exportTXT(liste, nomFichier))
    boutonExportText['font'] = fontButton
    boutonExportText.pack(pady=5, side=TOP)

    ## Bouton permettant d'ajouter un nouvel email dans la liste
    boutonAjouter = Button(fenetrePremiereListe, text = 'Ajouter un email', width=30, command = lambda: ajouter(liste, listBoxWhiteList1))
    boutonAjouter['font'] = fontButton
    boutonAjouter.pack(pady=5, side=TOP)

    ## Bouton permettant de modifier un email selectionné
    boutonModifier = Button(fenetrePremiereListe, text = 'Modifier l\'email', width=30, command = lambda: modifier(liste, listBoxWhiteList1))
    boutonModifier['font'] = fontButton
    boutonModifier.pack(pady=5, side=TOP)

    ## Bouton permettant de supprimer un email selectionné
    boutonModifier = Button(fenetrePremiereListe, text = 'Supprimer l\'email', width=30, command = lambda: supprimer(liste, listBoxWhiteList1))
    boutonModifier['font'] = fontButton
    boutonModifier.pack(pady=5, side=TOP)
    
## Fonction permettant de remplir une ListBox
def remplir(listBox, uneListe):
    for item in uneListe:
        listBox.insert(END, item)

## Exportation en CSV
def exportCSV(liste, nomFichier):
    nomFichier +=  ".csv"
    with open(nomFichier, 'w') as csvfile:
        try:
            wrCSV = csv.writer(csvfile, delimiter = "\n", quoting=csv.QUOTE_ALL)
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
def ajouter(liste, listBox):
    valid = False
    while valid == False:
        email = tkSimpleDialog.askstring("Nouvel email", "Saisir l'email que vous voulez ajouter")
        if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None):
            liste.append(email)
            valid = True
            listBox.insert(END, email)
        else:
           tkMessagebox.showerror("Erreur de saisie","L'email n'est pas valide")
           print("erreur")

## Modifier un email
def modifier(uneListe, uneListBox):
    index = uneListBox.curselection()
    ## Verification qu'un élément est sélectionné dans la liste
    if index:
        selectionEmail = uneListBox.get(index[0])
        email = tkSimpleDialog.askstring("Nouvel email", "Saisir l'email que vous voulez modifier", initialvalue=selectionEmail)
        uneListBox.delete(index)
        if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None):
            uneListe.append(email)
            valid = True
            uneListBox.insert(END, email)
        else:
           tkMessagebox.showerror("Erreur de saisie","L'email n'est pas valide")
           print("erreur")
    else:
        print("erreur")

## Supprmier un email
def supprimer(liste, listBox):
    index = listBox.curselection()
    ## Verification qu'un élément est sélectionné dans la liste
    if index:
        selectionEmail = listBox.get(index[0])
        listBox.delete(index)
        liste.remove(selectionEmail)
    else:
        print("erreur")

## Importer en CSV
def importCSV():
    nomFichier = tkSimpleDialog.askstring("Fichier à ouvrir", "Saisir le nom du fichier CSV que vous voulez ouvrir")
    newList = nomFichier
    importedList = []
    nomFichier +=  ".csv"
    with open(nomFichier) as csvfile:
        readCSV = csv.reader(csvfile)
        print(readCSV)
        try:
            for row in readCSV:
                importedList.append(row)
                print(importedList)
            afficheListe(importedList, newList)
        except:
            print("erreur")
    csvfile.close()

## Exportation en texte
def importTXT():
    nomFichier = tkSimpleDialog.askstring("Fichier à ouvrir", "Saisir le nom du fichier texte que vous voulez ouvrir")
    newList = nomFichier
    importedList = []
    nomFichier += ".txt"
    txtFile = open(nomFichier, 'r')
    try:
        content = txtFile.readlines()
        print(content)
        for line in content:
            importedList.append(line)
            print(importedList)
        afficheListe(importedList, newList)
    except:
        tkMessagebox.showerror("Erreur de sauvegarde","Il y a une erreur lors de la sauvegarde")
    txtFile.close()

## Définition des listes
whiteList1 = ["martin.duouit@gmail.com", "Jdoe@gmail.com", "PaulDupuis@gmail.com", "charlotte.blanc@mail.fr", "martin.duouit@gmail.com", "claire.duval.com", "ahmed.zouaoui@mail.fr", "PaulDupuis@gmail.com"]
whiteList2 = ["test@test.com", "ahmed.zouaoui@mail.fr", "mail@gmail.com", "mail.mail.fr", "test@test.com", "blanche@free.fr", "anouk.zouaoui@gmail.com", "martin.duouit@gmail.com", "blanche@free.fr"]
blackList = ["test@test.com", "martin.duouit@gmail.com", "mail.mail.fr"]

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
Canevas.pack()

## Label du choix
label = Label(fenetre, text="Que souhaitez-vous faire? ")
label.configure(font=fontLabel)
label.pack()

## Création des boutons
## Bouton permettant d'afficher la première liste
boutonPremiereListe = Button(fenetre, text = 'Afficher la première liste', width=30,  command = lambda: afficheListe(whiteList1, 'first_white_list'))
boutonPremiereListe['font'] = fontButton
boutonPremiereListe.pack(pady=5)

## Bouton permettant d'afficher la deuxième liste
boutonDeuxiemeListe = Button(fenetre, text = 'Afficher la deuxième liste', width=30,  command = lambda: afficheListe(whiteList2, 'second_white_list'))
boutonDeuxiemeListe['font'] = fontButton
boutonDeuxiemeListe.pack(pady=5)

## Bouton permettant d'afficher la liste noir
boutonBlackList = Button(fenetre, text = 'Afficher la liste noire', width=30, command = lambda: afficheListe(whiteList2, 'black_list'))
boutonBlackList['font'] = fontButton
boutonBlackList.pack(pady=5)

## Bouton permettant d'importer une liste à partir d'un fichier CSV
boutonBlackList = Button(fenetre, text = 'Importer à partir d\'un CSV', width=30, command = importCSV)
boutonBlackList['font'] = fontButton
boutonBlackList.pack(pady=5)

## Bouton permettant d'importer une liste à partir d'un fichier texte
boutonBlackList = Button(fenetre, text = 'Importer à partir d\'un fichier texte', width=30, command = importTXT)
boutonBlackList['font'] = fontButton
boutonBlackList.pack(pady=5)

fenetre.mainloop()
