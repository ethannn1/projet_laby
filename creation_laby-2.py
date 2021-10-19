# importation des bibliothèques
import networkx as nx
import matplotlib.pyplot as plt
import random
import affichage_laby as aff


def creer_labyrinthe(nb_lignes, nb_colonnes, murs=False):
    """
    """
    # Création du labyrinthe
    Laby = nx.Graph()
    # Initialisation du nom des sommets
    nb = 0

    # Création de tout les sommets
    for x in range(nb_colonnes):
        for y in range(nb_lignes):
            Laby.add_node(nb)
            nb += 1
    if not murs:
        # Création des arretes
        for node in Laby.nodes:
            # Si le sommet a un voisin de gauche
            if node % nb_colonnes > 0:
                Laby.add_edge(node, node - 1)  # On crée un lien entre le sommet et son voisin de gauche
            # Sinon, il a un voisin de droite
            else:
                Laby.add_edge(node, node + 1)  # On crée un lien entre le sommet et son voisin de droite
            # Si le sommet a un voisin en dessous de lui
            if node > nb_colonnes:
                Laby.add_edge(node, node - nb_colonnes)  # On crée un lien entre le sommet et son voisin d'en dessous

            else:
                Laby.add_edge(node, node + nb_colonnes)  # On crée un lien entre le sommet et son voisin d'au dessus

    return Laby


def termine(dico_valeurs):
    valeurs = list(dico_valeurs.values())
    v1 = valeurs[0]
    for v in valeurs:
        if v != v1:
            return False
    return True

def trouve_voisin(val, nb_lignes, nb_colonnes):
    voisins = []
    if val%nb_colonnes>0:
        voisins.append(val-1)
    if val % nb_colonnes < nb_colonnes-1:
        voisins.append(val+1)
    if val>nb_colonnes-1:
        voisins.append(val - nb_colonnes)
    if val<nb_colonnes*nb_lignes - nb_colonnes:
        voisins.append(val + nb_colonnes)
    return voisins

def trouve_liaisons(nodes, arretes, valeur_noeuds, nb_lignes, nb_colonnes):
    v_n = 0
    while v_n != valeur_noeuds:

        v_n = valeur_noeuds.copy()

        for node in nodes:
            for voisin in trouve_voisin(node, nb_lignes, nb_colonnes):
                #print(node, trouve_voisin(node, nb_lignes, nb_colonnes))
                if (voisin, node) in arretes or (node, voisin) in arretes:
                    if valeur_noeuds[node] >valeur_noeuds[voisin]:
                        valeur_noeuds[node] = valeur_noeuds[voisin]
                    else:
                        valeur_noeuds[voisin] = valeur_noeuds[node]

        print(valeur_noeuds)


    return valeur_noeuds


def construction_laby(Laby, nb_lignes, nb_colonnes):

    #Création du dictionnaire
    valeur_noeuds = {}
    for node in Laby.nodes:
        valeur_noeuds[node] = node

    est_termine = termine(valeur_noeuds)
    while not est_termine:
        mur1 = random.randint(0,(nb_colonnes*nb_lignes)-1)
        mur2 = random.choice(trouve_voisin(mur1, nb_lignes, nb_colonnes))

        if valeur_noeuds[mur2] != valeur_noeuds[mur1]:
            print(mur1, mur2)
            Laby.add_edge(mur1, mur2)
            valeur_noeuds[mur1] = valeur_noeuds[mur2]
            print(Laby.edges)
            valeur_noeuds = trouve_liaisons(Laby.nodes, Laby.edges, valeur_noeuds, nb_lignes, nb_colonnes)

            #aff.afficher_labyrinthe(Laby, nb_colonnes, nb_lignes)
            print(valeur_noeuds)
            est_termine = termine(valeur_noeuds)

    return Laby


if __name__ == "__main__":
    nb_lignes, nb_colonnes = 5,3
    Laby = creer_labyrinthe(nb_lignes, nb_colonnes,True)
    Laby2 = construction_laby(Laby, nb_lignes, nb_colonnes)

    aff.afficher_labyrinthe(Laby, nb_colonnes, nb_lignes)