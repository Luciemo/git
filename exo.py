
#!/usr/local/bin/python3.9

liste = ["lapin", "chat", "chien", "chiot","dragon","ornithorynque"]
for i in liste:
                print(i)

#---------------- 2/ afficher de manière inversée
liste.reverse()
for i in liste:
                print(i)

#---------------- 3/ afficher de manière triée
liste.sort()
for i in liste:
                print(i)

#---------------- 4/ ajouter troll et supprimer animaux domestique
liste.append("troll")
liste_remove =["lapin","chat","chiot","chien"]

for i in liste_remove:
                liste.remove(i)

for i in liste:
                print(i)



#---------------- 5/ recherche séquentielle dans une liste non triée

from random import* # Package pour gérer le random
import random

# 10 numéros aléatoires
tab_jeu=[]
for i in range(0,10):
                     tab_jeu.append(random.randint(1,10))

print(tab_jeu)


# Choix du joueur
choix=int(input("\nTapez un numéro : "))

# Boucle de comparaison
for i in tab_jeu:
                 if choix ==i:
                              rep="gagné"
                              break
                 else:
                              rep="perdu"

                                                                                    # Réponse
print(rep)

##### boucle avec booléen
trouver = False

for i in tab_jeu:
                if i == choix:
                              trouver = True
                              break

if trouver:
           print("gagné")
else:
                                                                                               print("perdu")





                                                                                    #------------------ 5/ Recherche séquentielle dans une liste triée

                                                                                    # Choix du joueur
                                                                                    choix=int(input("\nTapez un numéro : "))

                                                                                    # 10 numéros aléatoires
                                                                                    tab_jeu=[]
                                                                                    for i in range(0,10):
                   tab_jeu.append(random.randint(1,10))
                 
print(tab_jeu)


                                                                                    #tri
                                                                                    tab_jeu.sort()
                                                                                    print(tab_jeu)

                                                                                    # Boucle de comparaison
                                                                                    for i in tab_jeu:
                                                                                                   if choix ==i:
                                                                                                               rep="gagné"
                           break
                                                                                                   elif choix <i:
                           rep="perdu"
                           break
                                                                                                   else:
                           rep="perdu"

                                                                                                                                                                        # Réponse
print(rep)
                                                                                                                                                                        ##### Boucle avec booléen
                                                                                    trouver = False
                                                                                    for i in tab_jeu:
                                                                                            if i <choix:
                    break
        elif i == choix:
                    trouver = True
                    break
if trouver:
          print("gagné")
else:
                                                                                              print("perdu")
