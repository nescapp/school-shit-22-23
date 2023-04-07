class GrandPere:
    
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme

class Ryad(GrandPere):
    
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme * 0.75

class Sefa(GrandPere):
    
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme * 0.25


if __name__ == "__main__": 
    grandpere = GrandPere("Simou", 50000)
    ryad = Ryad("Ryad", grandpere.somme)
    sefa = Sefa("Sefa", grandpere.somme)
    print(f"{grandpere.nom} a laissé {grandpere.somme}€ à ses petits-enfants")
    print(f"{ryad.nom} hérite de {ryad.somme}€")
    print(f"{sefa.nom} hérite de {sefa.somme}€")
