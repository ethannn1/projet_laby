#importation des bibliothèques
import networkx as nx
import random
import matplotlib.pyplot as plt

class Pile:
    """ classe Pile
        création d’une instance Pile avec une liste
    """
    def __init__(self):
        self.L = []
    
    def vide(self):
        return self.L == []
    
    def depiler(self):
        assert not self.vide(),"Pile vide"
        return self.L.pop()
    
    def sommet(self):
        assert not self.vide(),"Pile vide"
        return self.L[-1]
    
    def empiler(self,x):
        self.L.append(x)



def chercher_nx(laby:nx.Graph, source:int = None, destination:int = None)->list:
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
    
    
    return nx.shortest_path(laby, source, destination)

def chercher_dfs(G,source:int = None, destination:int = None)->list:
    nodes = list(Labyrinthe.nodes())
    # Si source n'est pas renseigné, alors on impose source = 0
    if source == None:
        source = nodes[0]
    # Si destination n'est pas renseigné, alors on impose destination = dernier sommet
    if destination == None:   
        destination = nodes[-1]
    
    sommets_visites=[]
    sommets_ferme=[]
    p=Pile()
    fin=False
    sommets_visites.append(source)
    p.empiler(source)
    while (not p.vide() and fin == False):
        tmp =p.sommet()
        voisins = []
        for v in Labyrinthe.neighbors(tmp):
            if v not in sommets_visites():
                voisins.append(v)
        if len(voisins)>0:
            for v in voisins:
                p.empiler(v)
                sommets_visites.append(v)
        else:
            sommets_visites=tmp
            p.depiler()
        
    return sommets_ferme

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
        # Affiche un itinéraire reliant le point de coordonnées (2,2) au point (6, 5) pour un labyrinthe 8*7
    itineraire = chercher_dfs(Labyrinthe, 3,11)
    print(itineraire)
    plt.clf() # Efface le dessin
    nx.draw(Labyrinthe, with_labels=True)
    plt.show()
    # Remarque: identifiant du sommet (2, 2) dans un labyrinthe 8*7 = 2*8 + 2 = 18
    # Identifiant du sommet (6, 5) dans un labyrinthe 8*7 = 6*8 + 5 = 53
