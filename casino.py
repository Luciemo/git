#!/usr/local/bin/python3.9

#-----------Packages------------------------
from math import* # Package pour gérer arrondir les gains
from random import* # Package pour gérer le random

#-- présentation texte-----------------------
print("\n\nBienvenue au casino !!!")
print("-----------------------")    
print("\nVous vous êtes installé à la table de la roulette avec 500 euros\n\n")
#------------------------choix et mise du joueur--------------------#
#cagnotte de départ
cagnotte = 500
reponse =str("o")




while reponse =="o":

    #case choisi
    case=int(input("\nChoisissez une case entre 0 et 49 : "))
    somme=int(input("\nTapez le montant de votre mise : "))
    pair= case%2


    if somme>cagnotte:
        print("\n Vous ne pouvez plus jouer, votre mise est trop élevée par rapport à ce qui vous reste dans votre cagnotte.")
    elif cagnotte==0:
        print("\n Vous ne pouvez plus jouer, votre cagnotte est vide !")
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
        print("\n\nLa roulette tourne...........")
        print("\n...........et s'arrete sur le numéro "+str(bille))
       
        gain=0

        if case =="bille":
                gain=ceil(3*somme)
                cagnotte= cagnotte+gain
                print("\nFélicitation !!! Vous obtenez " + str(gain) + " euros")
        else:
             if color_b =="color":
                       gain=ceil(0.5*somme)
                       cagnotte= cagnotte+gain
                       print("\nFélicitation !!! Vous obtenez " + str(gain) + " euros")
             else:
                       cagnotte=cagnotte-somme
                       print("\nDésolé vous avez perdu !")

        print("\nVotre cagnotte est dédormais de : " +str(cagnotte)+" euros\n")
    
        reponse = str(input("\nVoulez vous continuez ? o/n : "))
    
