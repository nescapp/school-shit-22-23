class GrandPere:
    """Classe définissant le grand-père"""
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme

class Ryad(GrandPere):
    """Classe définissant le petit-fils Ryad"""
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme * 0.75

class Sefa(GrandPere):
    """Classe définissant le petit-fils Sefa"""
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme * 0.25


if __name__ == "__main__": # Si le fichier est exécuté directement (et non importé)
    grandPere = GrandPere("Simou", 50000)
    ryad = Ryad("Ryad", grandPere.somme)
    sefa = Sefa("Sefa", grandPere.somme)
    print(f"\033[1m{grandPere.nom}\033[0m a laissé \033[1m{grandPere.somme}€\033[0m à ses petits-enfants")
    print(f"\033[1m{ryad.nom}\033[0m hérite de \033[1m{ryad.somme}€\033[0m")
    print(f"\033[1m{sefa.nom}\033[0m hérite de \033[1m{sefa.somme}€\033[0m")
