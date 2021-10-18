import networkx as nx
import matplotlib.pyplot as plt

class File:
    """ Classe File
        Création d’une instance File avec une liste
    """
    
    def __init__(self):
        self.L = []
        
    def vide(self):
        return self.L == []
    
    def defiler(self):
        assert not self.vide(), "file vide"
        return self.L.pop(0)
    
    def enfiler(self,x):
        self.L.append(x)
        
    def taille(self):
        return len(self.L)
    
    def sommet(self):
        return self.L[0]
    
    def present(self,x):
        return x in self.L

def chercher_bfs(laby:nx.Graph, source:int = None, destination:int = None)->list:
    """ Cherche le chemin le plus court entre les sommets source et destination
        selon le parcours en largeur.
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
        
    sommet_visite = []
    f = File()
    f.enfiler(source)

    while not f.vide():
        tmp = f.defiler()
        if tmp not in sommet_visite:
            sommet_visite.append(tmp)
        for voisin in laby.neighbors(tmp):
            if voisin not in sommet_visite and f.present(voisin) == False:
                f.enfiler(voisin)
        
    return sommet_visite

    
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
    chemin_bfs =chercher_bfs(Labyrinthe)
    print(chemin_bfs)
    itineraire = chercher_bfs(Labyrinthe, 3, 11)
    print(itineraire)
    plt.clf() # Efface le dessin
    nx.draw(Labyrinthe, with_labels=True)
    plt.show()