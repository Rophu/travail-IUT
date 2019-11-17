################################################
## Exercice sur les listes de listes          ##
################################################

# liste de listes pour le premier ascii art 
asciiart1=[[' ', '|', '\\', '/', '\\', '/', '\\', '/', '|', ' ', ' '],[' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '],\
   [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '], [' ', '|', ' ', '(', 'o', ')', '(', 'o', ')', ' ', ' '],\
   [' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '_', ')', ' '], [' ', ' ', '|', ' ', ',', '_', '_', '_', '|', ' ', ' '],\
   [' ', ' ', '|', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' '], [' ', '/', '_', '_', '_', '_', '\\', ' ', ' ', ' ', ' '],\
   ['/', ' ', ' ', ' ', ' ', ' ', ' ', '\\']]

# liste de listes pour le deuxième ascii art 
asciiart2=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', 'n', 'n', 'n', 'n', '_'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', 'G', 'G', 'G', 'G', 'M', 'M', 'b'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', 'p', '~', 'q', 'p', '~', '~', 'q', 'M', 'b'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', '|', '@', '|', '|', '@', ')', ' ', 'M', '|'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', ',', '-', '-', '-', '-', '.', 'J', 'M', '|'],\
    [' ', ' ', ' ', ' ', ' ', ' ', 'J', 'S', '^', '\\', '_', '_', '/', ' ', ' ', 'q', 'K', 'L'],\
    [' ', ' ', ' ', ' ', ' ', 'd', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', 'K', 'R', 'b'],\
    [' ', ' ', ' ', ' ', 'd', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', 'K', 'K', 'b'],\
    [' ', ' ', ' ', 'f', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', 'M', 'M', 'b'],\
    [' ', ' ', ' ', 'H', 'Z', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', 'M', 'M', 'M'],\
    [' ', ' ', ' ', 'F', 'q', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', 'M', 'M', 'M'],\
    [' ', '_', '_', '|', ' ', '"', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\\', 'd', 'S', '"', 'q', 'M', 'L'],\
    [' ', '|', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '`', "'", ' ', '\\', 'Z', 'q'],\
    ['_', ')', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '.', '_', '_', '_', '.', ',', '|', ' ', ' ', ' ', ' ', ' ', '.', "'"], \
    ['\\', '_', '_', '_', '_', ' ', ' ', ' ', ')', 'M', 'M', 'M', 'M', 'M', 'P', '|', ' ', ' ', ' ', '.', "'"],\
    [' ', ' ', ' ', ' ', ' ', '`', '-', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '-', '-', "'", ' ', 'h', 'j', 'm']]


def liste_de_listes_to_str(liste):
    """
    cette fonction transforme une liste de listes en une chaine de caractères
    où les éléments de la liste principale sont accolés sur une même ligne
    paramètre: liste, une liste de listes contenant des entiers
    résultat:"sous_liste_de_liste_en_str", une chaine de caractere des valeurs
            dans les sous-listes. Chaque sous-listes correspond à une ligne
    invariant: 
             
    """
    sous_liste_de_liste_en_str=''
    for sous_liste in liste:
        for i in range(len(sous_liste)):
            sous_liste_de_liste_en_str+=str(sous_liste[i])
        sous_liste_de_liste_en_str=sous_liste_de_liste_en_str+"\n"
    
    return sous_liste_de_liste_en_str
    
# A décommenter lorsque vous avez fini votre implémentation
assert liste_de_listes_to_str([])=='',"Pb appel liste_de_listes_to_str([])"
assert liste_de_listes_to_str([[0,1,2],[3,4,5],[6,7,8]])=='012\n345\n678\n', "Pb appel liste_de_listes_to_str([[0,1,2][3,4,5][6,7,8]])"
assert liste_de_listes_to_str([['X',' ','O'],['O','X',' '],['O',' ','X']])=='X O\nOX \nO X\n',"Pb appel liste_de_listes_to_str([['X',' ','O'],['O','X',' '],['O',' ','X']])"
print(liste_de_listes_to_str(asciiart1))
print(liste_de_listes_to_str(asciiart2))
# vos tests
assert liste_de_listes_to_str([[0,1,2],[],[6,7,8]])=='012\n\n678\n', "Pb appel liste_de_listes_to_str([[0,1,2][][6,7,8]])"
assert liste_de_listes_to_str([['X',' ','O'],['O','X',' '],[]])=='X O\nOX \n\n',"Pb appel liste_de_listes_to_str([['X',' ','O'],['O','X',' '],[]])"
def max_dans_liste_de_listes(liste):
    """
    retourne le plus grand élément d'une liste de listes
    paramètre:
    résultat:
    """
    max_de_liste_de_liste=None
    for sous_liste in liste:
        for i in range(len(sous_liste)):
            if max_de_liste_de_liste==None:
                max_de_liste_de_liste=sous_liste[i]
            else:
                if sous_liste[i]>max_de_liste_de_liste:
                    max_de_liste_de_liste=sous_liste[i]
    return max_de_liste_de_liste

# A décommenter lorsque vous avez fini votre implémentation
assert max_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])==8,"Pb appel max_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])"
assert max_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])==58,"Pb appel max_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])"
assert max_dans_liste_de_listes([])==None,"Pb appel max_dans_liste_de_listes([])"
# vos tests
assert max_dans_liste_de_listes([[0,1,2],[],[6,7,8]])==8,"Pb appel max_dans_liste_de_listes([[0,1,2],[],[6,7,8]])"
assert max_dans_liste_de_listes([[0,0,0],[58,58,58],[26,17,8]])==58,"Pb appel max_dans_liste_de_listes([[0,0,0],[58,58,58],[26,17,8]])"
assert max_dans_liste_de_listes([['X',' ','O'],['O','X',' '],[]])=='X',"Pb appel max_dans_liste_de_listes([['X',' ','O'],['O','X',' '],[]])"

def max_par_ligne_dans_liste_de_listes(liste):
    """
    retourne la liste des plus grands éléments de chaque ligne dans une liste de listes
    paramètre:
    résultat:
    """
    max_de_chaque_sous_liste=None
    liste_des_maximums=[]
    for sous_liste in liste:
        for i in range(len(sous_liste)):
            if max_de_chaque_sous_liste==None:
                max_de_chaque_sous_liste=sous_liste[i]
            else:
                if sous_liste[i]>max_de_chaque_sous_liste:
                    max_de_chaque_sous_liste=sous_liste[i]
        liste_des_maximums.append(max_de_chaque_sous_liste)
        max_de_chaque_sous_liste=None
        
    return liste_des_maximums
    
# A décommenter lorsque vous avez fini votre implémentation
assert max_par_ligne_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])==[2,5,8],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([[0,1,2],[3,4,5],[6,7,8]])"
assert max_par_ligne_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])==[25,58,26],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([[0,11,25],[7,14,58],[26,17,8]])"
assert max_par_ligne_dans_liste_de_listes([[45,1,24],[],[47,85,2,14]])==[45,None,85],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([[45,1,24],[],[47,85,2,14]])"
# vos tests
assert max_par_ligne_dans_liste_de_listes([[0,0,0],[0,0,0],[0,0,0]])==[0,0,0],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([[0,0,0],[0,0,0],[0,0,0]])"
assert max_par_ligne_dans_liste_de_listes([['X','a','x'],[58,58,58],['','','']])==['x',58,''],\
       "Pb Appel max_par_ligne_dans_liste_de_listes([['X','a','x'],[58,58,58],[26,17,8]])"
