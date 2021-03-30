#!/usr/local/bin/python3.9

#-----------Packages------------------------
from math import* # Package pour gérer arrondir les gains
from random import* # Package pour gérer le random

#-- présentation texte-----------------------
print("Bienvenue au casino !!!")
print("-----------------------")    
print("Vous vous êtes installé à la table de la roulette avec 500 euros")
print(" ")
print(" ")
#------------------------choix et mise du joueur--------------------#
#cagnotte de départ
cagnotte = 500
reponse =str("o")




while reponse =="o":

    #case choisi
    case=int(input("Choisissez une case entre 0 et 49 : "))
    print(" ")
    somme=int(input("Tapez le montant de votre mise : "))
    pair= case%2


    if somme>cagnotte:
        print(" ")
        print("Vous ne pouvez plus jouer, votre mise est trop élevée par rapport à ce qui vous reste dans votre cagnotte.")
    elif cagnotte==0:
        print(" ")
        print(" Vous ne pouvez plus jouer, votre cagnotte est vide !")
    else:


    #couleur choisi
        if pair =="0":                 # si pair
            color="b"
        else:
            color="r"


#--------------------roulette, choix aléatoire d'un numéro----------#
#numéro gagnant
        bille=int(randrange(50))
        pair_gagnant= bille%2
#couleur gagnante
        if pair_gagnant =="0":            # si pair
                  color_b="b"
        else:
                  color_b="r"

#--------------------Gains ---------------------------------------#
        gain=0

        if case =="bille":
                gain=ceil(3*somme)
                cagnotte= cagnotte+gain
        else:
             if color_b =="color":
                       gain=ceil(0.5*somme)
                       cagnotte= cagnotte+gain
             else:
                       cagnotte=cagnotte-somme
#-----------------affichage final ------------------------------#                       
        print(" ")
        print(" ")
        print("La roulette tourne........ et s'arrete sur le numéro "+str(bille))
        print(" ")
        print("Félicitation ! Vous obtenez " + str(gain))
        print(" ")
        print("Votre cagnotte est dédormais de : " +str(cagnotte)+" euros")
        print(" ")
        reponse = str(input("Voulez vous continuez ? o/n : "))
        print(" ")
