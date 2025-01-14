# numéro groupe : 94

import csv
from math import inf

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

def data_arcs_poids_to_dict(file_name):
    dict = {}
    with open(file_name, mode='r') as infile:
        reader = csv.reader(infile, delimiter=';')
        for row in reader:
            if dict.get(row[0]) == None and row[1] == 'favorise':
                dict[row[0]] = {row[2]:int(row[3])}
            elif row[1] == 'favorise':
                dict[row[0]][row[2]] = int(row[3])
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
    
    return calcul_plus_court_chemin(depart, dict_parents[fin][0], dict_parents ) + [fin]
    
def calcul_liste_2D(liste_paires_depart_arrivee):
    l = []
    for paire in liste_paires_depart_arrivee:
        chemin_calcule = calcul_plus_court_chemin(paire[0], paire[1], sous_graphe_parents(paire[0], csv_to_dict_favorise('data_arcs.csv')))
        if chemin_calcule is not None:
            l.append(chemin_calcule)
        else:
            l.append([])
    return l

def calcul_liste_longueurs(liste_paires_depart_arrivee):
    l = []
    for paire in liste_paires_depart_arrivee:
        if calcul_plus_court_chemin(paire[0], paire[1], sous_graphe_parents(paire[0], csv_to_dict_favorise('data_arcs.csv'))) == None:
            l.append(None)
        else:
            l.append(len(calcul_plus_court_chemin(paire[0], paire[1], sous_graphe_parents(paire[0], csv_to_dict_favorise('data_arcs.csv')))))
    return l

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = inf
    path = []
    for node in graph.keys():
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if shortest_distance.get(childNode) is None or shortest_distance.get(minNode) is None:
                pass
            elif weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        return path
    
print(dijkstra(data_arcs_poids_to_dict('data_arcs_poids.csv'), 'prunier', 'sauge'))