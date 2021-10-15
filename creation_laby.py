#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importation des bibliothèques
import networkx as nx
import matplotlib.pyplot as plt
import random

def creer_labyrinthe(nb_lignes, nb_colonnes, d):
    """ 
    """
    #Création du labyrinthe
    Laby = nx.Graph()
    #Initialisation du nom des sommets
    nb = 0
    
    #Création de tout les sommets
    for x in range(nb_colonnes):
        for y in range(nb_lignes):
            Laby.add_node(nb)
            nb+=1
    #Création des arretes
    for node in Laby.nodes:
        # Si le sommet a un voisin de gauche
        if node%nb_colonnes>0:
            Laby.add_edge(node,node-1) # On crée un lien entre le sommet et son voisin de gauche
        #Sinon, il a un voisin de droite
        else:
            Laby.add_edge(node,node+1)# On crée un lien entre le sommet et son voisin de droite
        #Si le sommet a un voisin en dessous de lui
        if node>nb_colonnes:
            Laby.add_edge(node,node-nb_colonnes) # On crée un lien entre le sommet et son voisin d'en dessous

        else:
            Laby.add_edge(node,node+nb_colonnes) # On crée un lien entre le sommet et son voisin d'au dessus
        
            
    return Laby
    
    
    
if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Laby = creer_labyrinthe(4, 3, 2)
    plt.clf() # Efface le dessin
    nx.draw(Laby, with_labels=True)
    plt.show()