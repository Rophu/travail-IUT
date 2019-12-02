'''
   -----------------------------------------
   Une troisième implémentation des matrices 2D en python
   -----------------------------------------
'''

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres:
    résultat:
    '''
    liste_valeur=[valeurParDefaut]*((nbLignes)*(nbColonnes))
    dicoMatrice={'lignes':nbLignes,'colonnes':nbColonnes,'valeur':listeValeur}
    
    return dicoMatrice

def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre:
    resultat:
    '''
    return dicoMatrice['lignes']

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre:
    resultat:    
    '''
    
    return dicoMatrice['colonnes']


def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres:
    resultat:        
    '''
    


def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres:
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''

    


