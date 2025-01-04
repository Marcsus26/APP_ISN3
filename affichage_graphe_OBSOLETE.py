import calcul

def afficher_liste_graphe(liste_ingrédients):
    for item in liste_ingrédients:
        print(item, end=" ")

afficher_liste_graphe(calcul.calcul_liste_2D([('prunier', 'sauge'), ('cardon', 'menthe'), ('pissenlit', 'trefle blanc')]))