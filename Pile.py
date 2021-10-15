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