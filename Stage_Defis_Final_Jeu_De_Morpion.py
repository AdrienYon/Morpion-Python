"""
@dev : Cela affiche la grille du Morpion qui se remplie au fur et à mesure
@params : Avec les boucles cela créer le grillage 
""" 
def afficher_grille(grille):
    print("     0)  1)  2)")
    print("   -------------") 
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print("  |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print("  |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print("  |")
    print("   -------------")

"""
@devs : Cela permet à la machine de demander aux joueurs d'entrée un numbre est dans le remplir dans la grille
@params : Elle peut exister avec la boucle while qui fait en sorte que la conditions ne soit remplis quand fin de partie
"""

def tour(grille, joueur):
    print("c'est ton tour joueur"+str(joueur))
    colonne = input("Veuillez entrez le numéro de la colone: ")
    ligne = input("Veuillez entrez le numero de la ligne: ")
    print("vous venez de choisir cette case ("+colonne+","+ligne+")")
    while grille [int(colonne)+int(ligne)*3]!=" ":
        afficher_grille(grille)
        print("cette case a deja était choisi, choisissez en une autre")
        colonne = input("Veuillez entrez le numéro de la colone: ")
        ligne = input("Veuillez entrez le numero de la ligne: ")
        print("vous venez de choisir cette case ("+colonne+","+ligne+")")

    if joueur == 1:
        grille[int(colonne)+int(ligne)*3]="X"
    if joueur == 2:
        grille[int(colonne)+int(ligne)*3]="O"
    afficher_grille(grille)

"""
@devs : Cette fonction permet de chercher des potentiels voisin dans les grilles remplis 
@params : Avec l'index des liste nous pouvons chercher les voisins
"""

def est_le_gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1 
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[1]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1

"""
@devs : Cela permet terminer la partie en annoncant le gagnant ou si toute la grille est remplie
@params : avec la variable grille et joueur
"""

def match_nul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1

joueur = 1
print("Le joueur 1 va jouer les X, et le joueur 2 les 0")
grille = [" "," "," "," "," "," "," "," "," "]
afficher_grille(grille)
gagne = 0
while gagne == 0:
    tour(grille,joueur)
    if est_le_gagnant(grille):
        print("LE JOUEUR"+str(joueur)+"REMPORTE LA PARTIE")
        gagne = 1
    else:
        if match_nul(grille):
            print("Plus de case disponibles, Mathc Nul.")
            gagne = 1
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1
  