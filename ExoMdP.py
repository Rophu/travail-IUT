####################################################
###    FONCTIONS UTILISÉES DANS LE PROGRAMME     ###
####################################################

def comporte_au_moins_huit_caracteres(chaine):
    """
    verifie si chaine comporte au moins 8 caracteres
    paramètres formels: chaine, une chaine de caractères(type str)
    résultat: "chaine_de_au_moins_huit_caractere", un booléen. il est True
              si la chaine comporte au moins 8 caractères, False sinon
    invariant: le nombre de caractères inférieur à 8 dans chaine de 
                l'indice 0 à 'indice'-1
    """
    indice=0
    chaine_de_au_moins_huit_caractere=False
    while  indice<len(chaine) and not chaine_de_au_moins_huit_caractere:
        if indice>7:
            chaine_de_au_moins_huit_caractere=True
        indice+=1
    return chaine_de_au_moins_huit_caractere
assert comporte_au_moins_huit_caracteres('')==False,'problème'
assert comporte_au_moins_huit_caracteres('vbsgbighswgshfglsrfng')==True,'problème'
assert comporte_au_moins_huit_caracteres('vbsgb')==False,'problème'

def comporte_au_moins_un_chiffre(chaine):
    """
    verifie si chaine comporte au moins 1 chiffre
    paramètres formels: chaine, une chaine de caractères(type str)
    résultat: "chaine_avec_au_moins_un_chiffre", un booléen. il est True
              si la chaine comporte au moins 1 chiffre, False sinon
    invariant: l'absence de chiffre dans chaine de l'indice 0 à 'indice'-1
    """
    indice=0
    chaine_avec_au_moins_un_chiffre=False
    while indice<len(chaine) and not chaine_avec_au_moins_un_chiffre:
        if chaine[indice].isnumeric():
            chaine_avec_au_moins_un_chiffre=True
        indice+=1
    return chaine_avec_au_moins_un_chiffre
assert comporte_au_moins_un_chiffre('nsdvnsdvlsvl1')==True,'Probleme'
assert comporte_au_moins_un_chiffre('nsdvnsdvlsvl')==False,'Probleme'

def ne_comporte_pas_d_espace(chaine):
    """
    verifie si chaine ne comporte pas d'espace
    paramètres formels: chaine, une chaine de caractères(type str)
    résultat: "chaine_sans_espace", un booléen. il est True
              si la chaine ne comporte pas d'espace, False sinon
    invariant: l'absence d'espace dans chaine de l'indice 0 à 'indice'-1
    """
    i=0
    chaine_sans_espace=True
    while i<len(chaine) and chaine_sans_espace:
        if chaine[i]==' ':
            chaine_sans_espace=False
        i+=1
        
    return chaine_sans_espace

assert ne_comporte_pas_d_espace('dqicbdsd qenfojcdnf')==False,'problème'
assert ne_comporte_pas_d_espace('dqicbdsdqenfojcdnf')==True,'problème'
assert ne_comporte_pas_d_espace('')==True,'problème'

def a_au_moins_une_majuscule(chaine):
    """
    verifie si chaine possède au moins une majuscule
    paramètres formels: chaine, une chaine de caractères(type str)
    résultat: "possede_au_moins_une_majuscule", un booléen. il est True
              si la chaine comporte au moins une majuscule, False sinon
    invariant: l'absence de majuscule dans chaine de l'indice 0 à 'indice'-1
    """
    i=0
    possede_au_moins_une_majuscule=False
    while i<len(chaine) and not possede_au_moins_une_majuscule:
        if chaine[i].isupper():
            possede_au_moins_une_majuscule=True
        i+=1
        
    return possede_au_moins_une_majuscule
    
assert a_au_moins_une_majuscule('dssfdsfAsds')==True,'problème'
assert a_au_moins_une_majuscule('dssfdsfasds')==False,'problème'
assert a_au_moins_une_majuscule('')==False,'problème'

def ne_possede_pas_deux_majuscules_consecutives(chaine):
    """
    verifie si chaine ne possède pas deux_majuscules_consecutives
    paramètres formels: chaine, une chaine de caractères(type str)
    résultat: "pas_deux_majuscules_dans_la_chaine", un booléen. il est True
              si la chaine comporte deux majuscules cons&écutives False sinon
    invariant: l'absence de majuscule consécutives dans chaine de l'indice
               0 à 'indice'-1
    """
    i=0
    pas_deux_majuscules_dans_la_chaine=True
    precedent_est_une_majuscule=False
    while i<len(chaine) and pas_deux_majuscules_dans_la_chaine:
        if chaine[i].isupper() and precedent_est_une_majuscule:
                pas_deux_majuscules_dans_la_chaine=False
        else:
            if chaine[i].isupper():
                precedent=chaine[i]
                precedent_est_une_majuscule=True
            else:
                precedent_est_une_majuscule=False
        i+=1
    return pas_deux_majuscules_dans_la_chaine

assert ne_possede_pas_deux_majuscules_consecutives('dlndRRdvjlvfnd')==False
assert ne_possede_pas_deux_majuscules_consecutives('dlndRdvjlvfnd')==True
assert ne_possede_pas_deux_majuscules_consecutives('AdlndRdVjlvfnA')==True
assert ne_possede_pas_deux_majuscules_consecutives('ERdlnddvjlvfnd')==False
assert ne_possede_pas_deux_majuscules_consecutives('dlnddvjlvfndRT')==False
assert ne_possede_pas_deux_majuscules_consecutives('')==True


def pas_de_caractere_de_ponctuation_dans_la_chaine(chaine):
    """
    verifie si chaine ne possède pas de caracteres de ponctuation 
    paramètres formels: chaine, une chaine de caractères(type str)
    résultat: "chaine_sans_ponctuation", un booléen. il est True
              si la chaine n'a pas de carctères de ponctuation False sinon
    invariant: l'absence de caractere de ponctuation dans chaine de l'indice
               0 à 'indice'-1
    """
    i=0
    ponctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    chaine_sans_ponctuation=True
    while i<len(chaine) and chaine_sans_ponctuation:
        if chaine[i] in ponctuation:
            chaine_sans_ponctuation=False
        i+=1
    return chaine_sans_ponctuation

assert pas_de_caractere_de_ponctuation_dans_la_chaine('ddqsfsrshsdf')==True
assert pas_de_caractere_de_ponctuation_dans_la_chaine('ddqsfsrs;hsdf')==False
assert pas_de_caractere_de_ponctuation_dans_la_chaine('dd(qsfsrshsdf')==False
assert pas_de_caractere_de_ponctuation_dans_la_chaine(',dqsfsrshsdf')==False
assert pas_de_caractere_de_ponctuation_dans_la_chaine('ddqsfsrshsd!')==False


####################################################
### PROGRAMME PRINCIPAL                          ###
####################################################
mot_de_passe_incorrect=True
while mot_de_passe_incorrect:
    rep=input('Entrez votre mot de passe: ')
    if comporte_au_moins_huit_caracteres(rep)==False:
        print("désolé, votre mot de passe doit comporter au moins 8 caractères")
    else:
        if comporte_au_moins_un_chiffre(rep)==False:
            print("désolé, votre mot de passe doit comporter au moins un chiffre")
        else:
            if ne_comporte_pas_d_espace(rep)==False:
               print("désolé, votre mot de passe ne doit pas comporter d’espace")
            else:
                if a_au_moins_une_majuscule(rep)==False:
                    print("désolé, votre mot de passe doit comporter au moins une majuscule")
                else:
                    if ne_possede_pas_deux_majuscules_consecutives(rep)==False:
                        print("désolé, votre mot de passe ne doit pas comporter deux majuscules consécutives")
                    else:
                        if pas_de_caractere_de_ponctuation_dans_la_chaine(rep)==False:
                            print("désolé, votre mot de passe ne doit pas comporter de ponctuation")
                        else:
                            print("Votre mot de passe est correct. Quand vous voulez, vous pouvez !")
                            mot_de_passe_incorrect=False
            
            
            



