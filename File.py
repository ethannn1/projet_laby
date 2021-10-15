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