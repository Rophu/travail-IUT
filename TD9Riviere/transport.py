#! /usr/bin/python3

def Personne(nom,age,moyen):
    """
    creer une personne qui doit être représentée par un dictionnaire
    paramètres: nom: nom de la personne, chaine de type str
                age:age de la personne, nombre de type int 
                moyen: nom du moyen de transport, chaine de type str
    resultat: un dictionnaire avec les différents paramètres en clefs et en
    valeurs, les données correspondantes
    """
    dicoPersonne={}
    dicoPersonne['nom']=nom
    dicoPersonne['age']=age
    dicoPersonne['moyen']=moyen
    
    return dicoPersonne

def get_nom(pers):
    """
    retourne le nom de la personne
    """
    return pers['nom']

def get_age(pers):
    """
    retourne l'age de la personne
    """
    return pers['age']

def get_moyen_transport(pers):
    """
    retourne le moyen de transport utilisé par la personne
    """
    return pers['moyen']

def set_nom(pers,nom):
    """
    change le nom de la persone
    """
    pers['nom']=nom

def set_age(pers,age):
    """
    change l'age de la personne
    """
    pers['age']=age

def set_moyen_transport(pers,moyen):
    """ 
    change le moyen de transport de la personne
    """
    pers['moyen']=moyen

def affiche_personne(pers):
    """
    affiche une personne
    """
    print('-'*10)
    print('Nom:',get_nom(pers))
    print('Age:',get_age(pers))
    print('Moyen de transport:', get_moyen_transport(pers))
    print('-'*10)


def lire_fichier_personnes(nom_fic):
    """
    lit une liste de personnes contenue dans un fichier
    """
    fic=open(nom_fic)
    liste_pers=[]
    for ligne in fic:
        [nom,age,moyen_trans]=ligne[:len(ligne)-1].split(',')
        liste_pers.append(Personne(nom,age,moyen_trans))
    fic.close()
    return liste_pers

def affiche_liste_personnes(liste_pers):
    """
    affiche une liste de personnes
    """
    print(liste_pers)

def age_moyen_utilisateur_transport(liste_pers,nom_moyen_transport):
    """
    retourne l'age moyen des personnes qui utilise comme moyen de transport
    celui passé en paramètres. Si aucune personne n'utilise ce moyen de transport
    la fonction doit retourner -1
    """
    moyenne_age_usager=-1
    somme_age=0
    nombre_usager=0
    for dictionnaire in liste_pers:
        for (clé,valeur) in dictionnaire.items():
            if clé=='age' and dictionnaire['moyen']==nom_moyen_transport:
                somme_age+=valeur
                nombre_usager+=1
    if somme_age != 0:
        moyenne_age_usager=somme_age//nombre_usager
        
    return moyenne_age_usager 
    
def liste_moyens_transport(liste_pers):
    """
    retourne sous la forme d'une liste de chaines de caractères la liste des 
    moyens de transport utilisés par les personne de listePers
    """
    liste_moyen_transport=[]
    for dictionnaire in liste_pers:
            for (clé,valeur) in dictionnaire.items():
                if clé=='moyen' and valeur not in liste_moyen_transport:
                    liste_moyen_transport.append(valeur)
       
    return liste_moyen_transport
        

### programme principal
if __name__=='__main__':
    lire_fichier_personnes('personnes.txt')
    #ajoutez vos appels aux fonctions sur les personnes
