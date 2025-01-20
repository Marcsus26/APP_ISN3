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
            graphe_liste.append(calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][0], liste_départs_arrivees[i][1], calcul.sous_graphe_parents(liste_départs_arrivees[i][0], calcul.csv_to_dict_favorise('data_arcs.csv'))))
            graphe_liste.append(calcul.calcul_plus_court_chemin(liste_départs_arrivees[i][1], liste_départs_arrivees[i][0], calcul.sous_graphe_parents(liste_départs_arrivees[i][1], calcul.csv_to_dict_favorise('data_arcs.csv'))))
        elif i >= 1 and len(calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][0], liste_départs_arrivees[i][1])) != 0 and len(calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][1], liste_départs_arrivees[i][0])) != 0 :
            for path in calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][0], liste_départs_arrivees[i][1]):
                if len(set(path).intersection(set(sum(graphe_liste, [])))) != 0:
                    graphe_liste.append(path)
                    boolean4 = True
                    break
            else:
                print("Pas de chemin trouvé qui satisfait toutes les conditions")
                return False
            for path in calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][1], liste_départs_arrivees[i][0]):
                if boolean4 or len(set(path).intersection(set(sum(graphe_liste, [])))) != 0:
                    graphe_liste.append(path)
                    break
            else:
                print("Pas de chemin trouvé qui satisfait toutes les conditions")
                return False
        else:
            print("Pas de chemin trouvé qui satisfait toutes les conditions")
            return False
    # print(graphe_liste)
    G = nx.DiGraph()
    for liste in graphe_liste:
        for i in range(len(liste) - 1):
            if liste[i] != liste[i + 1]:
                G.add_edge(liste[i], liste[i + 1])
        pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1400, node_color='skyblue', font_color='black', font_weight='bold', arrowsize = 20)
    plt.show()
    return True

# dijkstra ne supporte pas les parcelles adjacentes
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
        elif i >= 1 and len(calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][0], liste_départs_arrivees[i][1])) != 0 and len(calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][1], liste_départs_arrivees[i][0])) != 0 :
            for path in calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][0], liste_départs_arrivees[i][1]):
                if len(set(path).intersection(set(graphe_liste))) != set():
                    graphe_liste += path
                    break
            for path in calcul.find_all_paths_nx(calcul.csv_to_dict_favorise("data_arcs.csv"), liste_départs_arrivees[i][1], liste_départs_arrivees[i][0]):
                if len(set(path).intersection(set(graphe_liste))) != set():
                    graphe_liste += path
                    break
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

afficher_graphe([('fraisier des bois', 'pommier'), ('prunier', 'kiwi')])