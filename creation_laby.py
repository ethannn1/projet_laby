#importation des bibliothèques
import networkx as nx
import matplotlib.pyplot as plt
import random



def creer_labyrinthe(nb_lignes, nb_colonnes, murs=False):
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
    if not murs:
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

def termine(dico_valeurs):
    valeurs = list(dico_valeurs.values())
    v1 = valeurs[0]
    for v in valeurs:
        if v != v1:
            return False
    return True

def construction_laby(Laby,nb_lignes, nb_colonnes):
    Laby2 = creer_labyrinthe(nb_lignes, nb_colonnes,True)
    valeur_noeuds = {}
    for node in Laby.nodes:
        valeur_noeuds[node] = node

    est_termine = termine(valeur_noeuds)
    while not est_termine:
        arretes = list(Laby.edges)
        mur = random.choice(arretes)
        if valeur_noeuds[mur[0]] != valeur_noeuds[mur[1]]:
            Laby.remove_edge(mur[0],mur[1])
            arretes.remove(mur)
            Laby2.add_edge(mur[0], mur[1])
            valeur_noeuds[mur[0]] = valeur_noeuds[mur[1]]

            for node in Laby.nodes:
                node1 = node
                if node%nb_colonnes>0:
                    node2 = node1 - 1
                    if (node1, node2) in arretes or (node2, node1) in arretes:
                        valeur_noeuds[node1] = valeur_noeuds[node2]
                else:
                    node2 = node1 - 1
                    if (node1, node2) in arretes or (node2, node1) in arretes:
                        valeur_noeuds[node1] = valeur_noeuds[node2]
                    
                if node>nb_colonnes:
                    node2 = node1 - nb_colonnes
                    if (node1, node2) in arretes or (node2, node1) in arretes:
                        valeur_noeuds[node1] = valeur_noeuds[node2]
                else:
                    node2 = node1 + nb_colonnes
                    if (node1, node2) in arretes or (node2, node1) in arretes:
                        valeur_noeuds[node1] = valeur_noeuds[node2]
                        
        est_termine = termine(valeur_noeuds)  
        print(valeur_noeuds.values())
    return Laby2
        
    
    
if __name__ == "__main__":
    nb_lignes, nb_colonnes = 3, 2
    Laby = creer_labyrinthe(nb_lignes, nb_colonnes)
    Laby2 = construction_laby(Laby, nb_lignes, nb_colonnes)

    nx.draw(Laby2, with_labels=True)
    plt.show()