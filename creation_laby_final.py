# importation des bibliothèques
import networkx as nx
import random
import affichage_laby as aff

def termine(dico_valeurs:dict) -> bool:
    """ Renvoie True si toutes les valeurs d'un dictionnaire sont identiques et False sinon
        Permet de vérifier si le labyrinthe est connexe"""
    valeurs = list(dico_valeurs.values())
    v1 = valeurs[0]
    for v in valeurs:
        if v != v1:
            return False
    return True

def trouve_voisin(node:int, nb_lignes:int, nb_colonnes:int) -> list:
    """Renvoie la liste de tout les voisins du noeud mis en paramètre"""
    voisins = []
    if node%nb_colonnes>0:
        voisins.append(node - 1)
    if node % nb_colonnes < nb_colonnes-1:
        voisins.append(node + 1)
    if node>nb_colonnes-1:
        voisins.append(node - nb_colonnes)
    if node<nb_colonnes*nb_lignes - nb_colonnes:
        voisins.append(node + nb_colonnes)
    return voisins

def trouve_liaisons(nodes:list, arretes:list, valeur_noeuds:dict, nb_lignes:int, nb_colonnes:int) -> dict:
    """ Met la même valeur a tout les noeuds qui sont reliés
        Renvoie le dictionnaire qui contient les valeurs de chaque noeud"""
    v_n = 0
    while v_n != valeur_noeuds:
        v_n = valeur_noeuds.copy()

        for node in nodes:
            for voisin in trouve_voisin(node, nb_lignes, nb_colonnes):
                if (voisin, node) in arretes or (node, voisin) in arretes:
                    if valeur_noeuds[node] >valeur_noeuds[voisin]:
                        valeur_noeuds[node] = valeur_noeuds[voisin]
                    else:
                        valeur_noeuds[voisin] = valeur_noeuds[node]
    return valeur_noeuds

def construction_laby(nb_lignes:int, nb_colonnes:int, prc_degradation:int=0) -> nx.Graph:
    """ Crée un labyrinthe de nb_lignes lignes et nb_colonnes colonnes
        avec une degradation de prc_degradation en %.
        Renvoie le labyrinthe sous forme de graphe networkx"""

    Laby = nx.Graph()
    nb = 0
    # Création de tout les sommets
    for x in range(nb_colonnes):
        for y in range(nb_lignes):
            Laby.add_node(nb)
            nb += 1

    #Création du dictionnaire
    valeur_noeuds = {}
    for node in Laby.nodes:
        valeur_noeuds[node] = node

    while not termine(valeur_noeuds): # Continue tant que le labyrinthe n'est pas connexe
        # On prend 2 noeuds adjacents au hasard
        node1 = random.randint(0,(nb_colonnes*nb_lignes)-1)
        node2 = random.choice(trouve_voisin(node1, nb_lignes, nb_colonnes))

        # Si ils n'ont pas la même valeur on relie les deux et on met a jour la valeurs des noeuds du labyrinthe
        if valeur_noeuds[node2] != valeur_noeuds[node1]:
            Laby.add_edge(node1, node2)
            valeur_noeuds[node1] = valeur_noeuds[node2]
            valeur_noeuds = trouve_liaisons(Laby.nodes, Laby.edges, valeur_noeuds, nb_lignes, nb_colonnes)

    if prc_degradation>100: # On fait que prc_degradation ne soit pas supérieur à 100
        prc_degradation = 100

    # On calcule le nombre de liaisons possible que peut avoir le labyrinthe
    nb_liaisons_possibles = (nb_lignes-1) * nb_colonnes + nb_lignes * (nb_colonnes-1)
    # On calcule combien de murs on doit casser
    nb_murs_a_casser = round((prc_degradation / 100) * (nb_liaisons_possibles - len(Laby.edges)))

    for i in range(nb_murs_a_casser):
        node1 = random.randint(0,(nb_colonnes*nb_lignes)-1)
        node2 = random.choice(trouve_voisin(node1, nb_lignes, nb_colonnes))

        while (node1, node2) in Laby.edges or (node2, node1) in Laby.edges:  # Jusqu'à trouver deux noeuds pas liés
            node1 = random.randint(0, (nb_colonnes * nb_lignes) - 1)
            node2 = random.choice(trouve_voisin(node1, nb_lignes, nb_colonnes))
        Laby.add_edge(node1,node2) # On lie les deux noeuds

    return Laby # On renvoie le labyrinthe final

# On crée un labyrinthe de test
if __name__ == "__main__":
    nb_lignes, nb_colonnes = 7,6
    Laby = construction_laby(nb_lignes, nb_colonnes, 10)
    aff.afficher_labyrinthe(Laby, nb_colonnes, nb_lignes)