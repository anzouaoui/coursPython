##Ecrire le jour de la semaine en fonction de la date
dicMois = {'01':0, '02':3, '03':3, '04':6, '05':1, '06':4, '07':6, '08':2, '09':5, '10':0, '11':3, '12':5}
dicSiecle = {'16':0, '17':4, '18':2, '19':0, '20':6, '21':4}
dicJours = {0:'Dimanche', 1:'Lundi', 2:'Mardi', 3:'Mercredi', 4:'Jeudi', 5:'Vendredi', 6:'Samedi'}
date = input("Saisir la date (jj/mm/aaaa): ")
somme = 0
jour = date[0:2]
mois = date[3:5]
annee = int(date[8:])
anneeComplet = int(date[6:])

if anneeComplet%4 == 0:
    if(anneeComplet%100 == 0 or anneeComplet%400 == 0):
        print("l'annee est bissextile")
        if (mois == '01' or mois == '02'):
            somme = annee + (annee//4) + int(jour) + int(dicMois[mois]) - 1
else:
    print("l'annee n'est pas bissextile")

somme = annee + (annee//4) + int(jour) + int(dicMois[mois]) + dicSiecle[date[6:8]]
jourFinal = somme % 7
print(dicJours[jourFinal])

