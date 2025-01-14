import networkx as nx
import matplotlib.pyplot as plt
import calcul

def afficher_graphe(liste_départs_arrivees):
    # graphe_liste = calcul.calcul_liste_2D([(depart, arrivee)])[0] + calcul.calcul_liste_2D([(arrivee, depart)])[0]
    graphe_liste = []
    for i in range(len(liste_départs_arrivees)):
        boolean1 = calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][0], liste_départs_arrivees[i][1], calcul.sous_graphe_parents(liste_départs_arrivees[i][0], calcul.csv_to_dict_favorise('data_arcs.csv'))) is not None
        boolean2 = calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][1], liste_départs_arrivees[i][0], calcul.sous_graphe_parents(liste_départs_arrivees[i][1], calcul.csv_to_dict_favorise('data_arcs.csv'))) is not None
        boolean3 = boolean1 and boolean2
        # print(graphe_liste)
        if i == 0 and boolean3:
            graphe_liste += calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][0], liste_départs_arrivees[i][1], calcul.sous_graphe_parents(liste_départs_arrivees[i][0], calcul.csv_to_dict_favorise('data_arcs.csv')))
            if boolean2:
                graphe_liste += calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][1], liste_départs_arrivees[i][0], calcul.sous_graphe_parents(liste_départs_arrivees[i][1], calcul.csv_to_dict_favorise('data_arcs.csv')))
        elif boolean3 and len(set(calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][0], liste_départs_arrivees[i][1], calcul.sous_graphe_parents(liste_départs_arrivees[i][0], calcul.csv_to_dict_favorise('data_arcs.csv')))).intersection(set(graphe_liste))) != set() and len(set(calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][1], liste_départs_arrivees[i][0], calcul.sous_graphe_parents(liste_départs_arrivees[i][1], calcul.csv_to_dict_favorise('data_arcs.csv')))).intersection(set(graphe_liste))) != set():
            graphe_liste += calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][0], liste_départs_arrivees[i][1], calcul.sous_graphe_parents(liste_départs_arrivees[i][0], calcul.csv_to_dict_favorise('data_arcs.csv')))
            if boolean2:
                graphe_liste += calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][1], liste_départs_arrivees[i][0], calcul.sous_graphe_parents(liste_départs_arrivees[i][1], calcul.csv_to_dict_favorise('data_arcs.csv')))
        else:
            print("Pas de chemin trouvé qui satisfait les conditions")
            return False
    G = nx.DiGraph()
    for i in range(len(graphe_liste) - 1):
        if graphe_liste[i] != graphe_liste[i + 1]:
            G.add_edge(graphe_liste[i], graphe_liste[i + 1])
        pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1400, node_color='skyblue', font_color='black', font_weight='bold', arrowsize = 20)
    plt.show()
    return True

def afficher_graphe_dijkstra(liste_départs_arrivees):
    # graphe_liste = calcul.calcul_liste_2D([(depart, arrivee)])[0] + calcul.calcul_liste_2D([(arrivee, depart)])[0]
    graphe_liste = []
    for i in range(len(liste_départs_arrivees)):
        boolean1 = calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][0], liste_départs_arrivees[i][1]) is not None
        boolean2 = calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][1], liste_départs_arrivees[i][0]) is not None
        boolean3 = boolean1 and boolean2
        # print(graphe_liste)
        if i == 0 and boolean3:
            graphe_liste += calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][0], liste_départs_arrivees[i][1])
            if boolean2:
                graphe_liste += calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][1], liste_départs_arrivees[i][0])
        elif boolean3 and len(set(calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][0], liste_départs_arrivees[i][1])).intersection(set(graphe_liste))) != set() and len(set(calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][1], liste_départs_arrivees[i][0])).intersection(set(graphe_liste))) != set():
            graphe_liste += calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][0], liste_départs_arrivees[i][1])
            if boolean2:
                graphe_liste += calcul.dijkstra(calcul.data_arcs_poids_to_dict('data_arcs_poids.csv'),liste_départs_arrivees[i][1], liste_départs_arrivees[i][0])
        else:
            print("Pas de chemin trouvé qui satisfait les conditions")
            return False
    G = nx.DiGraph()
    for i in range(len(graphe_liste) - 1):
        if graphe_liste[i] != graphe_liste[i + 1]:
            G.add_edge(graphe_liste[i], graphe_liste[i + 1])
        pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1400, node_color='skyblue', font_color='black', font_weight='bold', arrowsize = 20)
    plt.show()
    return True

# afficher_graphe_dijkstra([('fraisier des bois', 'pommier'), ('prunier', 'kiwi')])
