import networkx as nx
import matplotlib.pyplot as plt
import calcul

def afficher_graphe(liste_départs_arrivees):
    # graphe_liste = calcul.calcul_liste_2D([(depart, arrivee)])[0] + calcul.calcul_liste_2D([(arrivee, depart)])[0]
    graphe_liste = []
    for i in range(len(liste_départs_arrivees)):
        graphe_liste += calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][0], liste_départs_arrivees[i][1], calcul.sous_graphe_parents(liste_départs_arrivees[i][0], calcul.csv_to_dict_favorise('data_arcs.csv')))
        graphe_liste += calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][1], liste_départs_arrivees[i][0], calcul.sous_graphe_parents(liste_départs_arrivees[i][1], calcul.csv_to_dict_favorise('data_arcs.csv')))
    G = nx.DiGraph()
    for i in range(len(graphe_liste) - 1):
        if graphe_liste[i] != graphe_liste[i + 1]:
            G.add_edge(graphe_liste[i], graphe_liste[i + 1])
        pos = nx.circular_layout(G)
    # if graphe_liste[0] == graphe_liste[len(graphe_liste) - 1]:
    # recode if statement to check if there is atleast 1 element in common between the two paths
    nx.draw(G, pos, with_labels=True, node_size=1400, node_color='skyblue', font_color='black', font_weight='bold', arrowsize = 20)
    plt.show()
    return True
    # else:
    #     print("Pas de chemin trouvé")
    #     return False

afficher_graphe([('prunier', 'sauge'), ('pissenlit', 'trefle blanc')]) 
