#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importation des bibliothèques
import networkx as nx
from Pile import *

def chercher_dfs(laby:nx.Graph, source:int = None, destination:int = None)->list:
    """ Cherche le chemin le plus court entre les sommets source et destination
        selon le parcours en profondeur.
    """
    # Initialisation des sommets source et destination s'ils ne sont pas renseignés
    # Récupère la liste des sommets
    nodes = list(laby.nodes())
    # Si source n'est pas renseigné, alors on impose source = 0
    if source == None:
        source = nodes[0]
    # Si destination n'est pas renseigné, alors on impose destination = dernier sommet
    if destination == None:   
        destination = nodes[-1]
    
    sommets_visites = []
    sommets_fermes = []
    p = Pile()
    sommet.append(sommets_visites)
    p.empile(sommet)
    while not p.vide():
        tmp=p
        voisins=
        if voisins  :
            v=
            sommets_visites=v
            p.empiler(v)
        else: 
            sommets_fermes=tmp
            p.depiler()


                  
    return sommet_fermes
    
    return nx.shortest_path(laby, source, destination)

if __name__ == "__main__":
    # Création du labyrinthe de test
    aretes = [(0, 1), (0, 4), (1, 0), (1, 5), (2, 6), (3, 7), (4, 0), (4, 5), (5, 1) , \
     (5, 4), (5, 6), (5, 9), (6, 2), (6, 5), (6, 7), (6, 10), (7, 3), (7, 6), (8, 9),\
     (9, 5), (9, 8), (9, 10), (10, 6), (10, 9), (10, 11), (11, 10)]
    colonnes = 4
    lignes = 3
    nb_sommets = colonnes * lignes
    noeuds = list(range(nb_sommets))
    Labyrinthe = nx.Graph()
    Labyrinthe.add_nodes_from(noeuds)
    Labyrinthe.add_edges_from(aretes)

    # Lance le test de la fonction afficher_labyrinthe()
    #afficher_labyrinthe(Labyrinthe, colonnes, lignes)
    chemin_dfs =chercher_dfs(Labyrinthe)
    print(chemin_dfs)