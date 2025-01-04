########################################################
import csv

# Definir ici la fonction calcul_liste_longueurs(liste_paires_depart_arrivee)
# qui lit le fichier 'data_arcs.csv' dans le repertoire courant puis
# calcule la longueur de plus court chemin pour chaque paire
# (depart, arrivee) de la liste liste_paires_depart_arrivee.
# Par convention cette longueur sera egale a None si il n'y a pas
# de chemin de 'depart' a 'arrivee'.
# Les plus courts chemins sont cherches en utilisant seulement les arcs
# 'favorise' du graphe.
# Lorsqu'elle se termine la fonction renvoie la liste des longueurs obtenues.

# Par exemple
# calcul_liste_longueurs([('prunier', 'sauge'), ('cardon', 'menthe'), ('pissenlit', 'trefle blanc')])
# renverra la liste [6, None, 4]

# Il est tout à fait possible de definir d'autres fonctions intermedaires
# pour ce calcul, par exemple pour lire le fichier ou pour calculer un plus
# court chemin pour une seule paire (depart, arrivee).

def csv_to_dict_favorise(file_name):
    dict = {}
    with open(file_name, mode='r') as infile:
        reader = csv.reader(infile, delimiter=';')
        for row in reader:
            if dict.get(row[0]) == None and row[1] == 'favorise':
                dict[row[0]] = [row[2]]
            elif row[1] == 'favorise':
                dict[row[0]].append(row[2])
    return dict

def sous_graphe_parents(s_init, adj):
    '''
    s_init : sommet initial
    adj : dico associant la liste des suivants à tout sommet ayant au moins un suivant
    type des sommets quelconques pourvu qu'il y ait cohérence entre éléments de la liste et du dico.
    retourne un dico représentant le sous-graphe des parents du graphe initial
    '''
    parents = {s_init : []}
    a_traiter = [s_init] #liste des sommets à traiter
    while a_traiter != [] :
        s = a_traiter.pop(0) #on retire le premier élément de la liste
        for suivant in adj.get(s, []) : #on récupère la liste des suivants de s, [] si s n'a pas de suivant
            if suivant not in parents :
                parents[suivant] = [s]
                a_traiter.append(suivant)
            else :
                parents[suivant].append(s)
    parents[s_init] = [] #on enlève le parent de s_init
    return parents

def calcul_plus_court_chemin(depart, fin , dict_parents):
    if dict_parents.get(fin) == None:
        return None
    
    elif dict_parents[fin] == [] :
        return [fin]
    
    else :
        return calcul_plus_court_chemin(depart, dict_parents[fin][0], dict_parents ) + [fin]
    

def calcul_liste_longueurs(liste_paires_depart_arrivee):
    l = []
    for paire in liste_paires_depart_arrivee:
        if calcul_plus_court_chemin(paire[0], paire[1], sous_graphe_parents(paire[0], csv_to_dict_favorise('data_arcs.csv'))) == None:
            l.append(None)
        else:
            l.append(len(calcul_plus_court_chemin(paire[0], paire[1], sous_graphe_parents(paire[0], csv_to_dict_favorise('data_arcs.csv')))))
    return l
# A DEFINIR ...

# UNE FOIS CETTE FONCTION DEFINIE, VOUS POUVEZ LA TESTER EN EXECUTANT
# DIRECTEMENT LE PROGRAMME CI-DESSOUS.


########################################################
# NE PAS MODIFIER LA PARTIE CI-DESSOUS, SAUF SI VOUS
# ETES DANS LE ROLE D'EVALUATEUR.
# SI VOUS ETES EVALUATEUR, LA SEULE MODIFICATION A APPORTER
# EST DE MODIFIER CI-DESSOUS LA LIGNE QUI INITIALISE LA
# VARIABLE reference_longueurs_chemins_min
# AFIN DE LA RENSEIGNER AVEC LE JEU DE TEST QUI SERA
# MIS A VOTRE DISPOSITION SUR MOODLE.
########################################################

def run_test():
    # Ce programme compare les longueurs des chemins minimaux renvoyées
    # par la fonction calcul_liste_longueurs(liste_paires_depart_arrivee)
    # aux longueurs correctes, stockées ci-dessous comme références
    # dans la variable reference_longueurs_chemins_min.

    # Exemple de petit jeu de test:
    #reference_longueurs_chemins_min = {('prunier', 'sauge'): 6, ('cardon', 'menthe'): None, ('pissenlit', 'trefle blanc'): 4}
    
    # Exemple de jeu de test plus gros:
    reference_longueurs_chemins_min = {('prunier', 'sauge'): 6, ('pissenlit', 'trefle blanc'): 4, ("oeillet d'inde", 'asperge'): None, ('ciboulette chinoise', 'marjolaine'): None, ('trefle blanc', 'panais'): 3, ('melon', 'trefle blanc'): 4, ('piment', 'poivron'): None, ('thym', "rosier d'inde"): 4, ('celeri', 'pissenlit'): 5, ('poivron', 'laitue'): 3, ('lavande', 'topinambour'): 4, ('courge', 'pissenlit'): 5, ('coriandre', 'tournesol'): 4, ('cardon', 'genet'): None, ('menthe', 'piment'): 5, ('mais', 'ciboulette chinoise'): 4, ('cosmos', 'thym'): 3, ("oeillet d'inde", 'patate douce'): None, ('basilic', 'pommier'): 4, ('cornichon', 'patate douce'): None, ('poireau', 'menthe'): None, ("rosier d'inde", 'pasteque'): None, ("oeillet d'inde", 'betterave'): None, ('laitue', 'cornichon'): 3, ('pasteque', 'panais'): 3, ('poivron', 'courgette'): 4, ('origan', 'haricot'): 3, ('carotte', 'groseillier'): 3, ('courge', 'radis'): 3, ('patate douce', 'melisse citronnelle'): 4, ('chou-rave', 'pomme de terre'): None, ('vigne', 'cassis'): 4, ('courgette', 'chenopode blanc'): 5, ('lin', 'cumin'): 4, ('agrume', 'morelle de balbis'): 6, ('cresson', 'sarriette'): 4, ('kiwi', 'artichaut'): 4, ('oignon', 'inule visqueuse'): 4, ('tanaisie commune', 'melisse citronnelle'): 5, ('aneth', 'lavande'): 5, ('anis', 'cumin'): 4, ('chenopode blanc', 'roquette'): None, ('lavande', 'sarriette'): 5, ('origan', 'courgette'): 4, ("oeillet d'inde", 'pomme de terre'): None, ('prunier', 'agrume'): 6, ('kiwi', 'poireau'): 4, ('persil', 'haricot'): 3, ('cerfeuil commun', 'olivier'): 5, ('sarrasin', 'menthe'): None}
    # IMPORTANT: Ce jeu vous permet de réaliser un test, mais c'est un jeu différent
    # qui sera transmis aux évaluateurs.
    
    liste_paires_depart_arrivee = list(reference_longueurs_chemins_min.keys())
    liste_longueurs_reference = list(reference_longueurs_chemins_min.values())
    
    liste_longueurs = calcul_liste_longueurs(liste_paires_depart_arrivee)
    
    nb_differences = 0
    for i, longueur_reference in enumerate(liste_longueurs_reference):
        if longueur_reference != liste_longueurs[i]:
            nb_differences += 1
            print("="*40)
            print(f"DIFFERENCE de nombre d'arcs pour la paire :")
            print(f"    depart={liste_paires_depart_arrivee[i]}")
            print(f"    arrivee={liste_paires_depart_arrivee[i]}")
            print(f"    reference={liste_longueurs_reference[i]}")
            print(f"    longueur={liste_longueurs[i]}")
    
    
    print()
    print("Les longueurs des chemins minimaux utilisant")
    print("les arcs 'favorise' pour les paires du jeu de test")
    if nb_differences == 0:
        print("sont toutes identiques a la version de reference.")
    else:
        print("NE SONT PAS TOUTES IDENTIQUES A LA VERSION DE REFERENCE !!!")

run_test()
# print(csv_to_dict_favorise('data_arcs.csv'))
# print(sous_graphe_parents('prunier', csv_to_dict_favorise('data_arcs.csv')))
# print(calcul_plus_court_chemin('prunier', 'sauge', sous_graphe_parents('prunier', csv_to_dict_favorise('data_arcs.csv'))))
# print(calcul_liste_longueurs([('prunier', 'sauge'), ('cardon', 'menthe'), ('pissenlit', 'trefle blanc')]))
