import numpy as np
import matplotlib.pyplot as plt
import sys
from termcolor import colored, cprint
import random as rd

#variable globale

NB_COLONNES = 7
NB_LIGNES = 6

Grille = np.zeros((NB_LIGNES,NB_COLONNES))
listeVect = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]


#fonctions de bases

def jouerColonne(Grille, joueur, colonne):
    i = 1
    while i <= NB_LIGNES and Grille[NB_LIGNES - i][colonne] != 0 :
        i += 1

    if i <= NB_LIGNES :
        Grille[NB_LIGNES - i][colonne] = joueur


def afficherGrille(Grille):
    for i in range(NB_LIGNES):
        text = ''
        for j in range(NB_COLONNES):
            if Grille[i][j] == 0 :
                text += 'O '

            if Grille[i][j] == 1 :
                text += colored('O ', 'red')

            if Grille[i][j] == -1 :
                text += colored('O ', 'yellow')
        print(text)

def gagner(Grille):
    for i in range(NB_LIGNES - 1, -1, -1):
        for j in range(NB_COLONNES):
            if Grille[i][j] != 0:
                joueur = Grille[i][j]
                for k in range(5):
                    vect = listeVect[k]
                    n = i + vect[0]
                    m = j + vect[1]
                    cpt = 1
                    while Grille[n][m] == joueur :
                        cpt += 1
                        n += vect[0]
                        m += vect[1]
                    if cpt >= 4 :
                        return joueur
    return 0


def partieRand(Grille):
    listeCol = [0,1,2,3,4,5,6]
    listeInd = [0,1,2,3,4,5,6]
    nb_col = NB_COLONNES

    joueurMain = 1

    while gagner(Grille) == 0 and len(listeCol) > 0:
        i = rd.randint(0,nb_col)
        col = listeCol[i]
        jouerColonne(Grille, joueurMain, col)

        if Grille[0][col] != 0:
            nb_col -= 1
            listeCol.pop(listeInd[col])
            j = col + 1
            while j < NB_COLONNES :
                listeInd -= 1




#ia




#main

jouerColonne(Grille,1, 2)
jouerColonne(Grille,-1, 3)
jouerColonne(Grille,1, 3)
jouerColonne(Grille,-1, 4)
jouerColonne(Grille,-1, 4)
jouerColonne(Grille,1, 4)
jouerColonne(Grille,-1, 5)
jouerColonne(Grille,-1, 5)
jouerColonne(Grille,-1, 5)




afficherGrille(Grille)
print(gagner(Grille))