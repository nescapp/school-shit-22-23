class Giraffe:
    """Classe représentant une girafe."""
    def __init__(self, nom, taches, poids, taille):
        # Attributs d'instance
        self.nom = nom
        self.taches = taches
        self.poids = poids
        self.taille = taille
        print(f"Je suis une girafe, je m'appelle {self.nom}.") # Affiche un message de création

    def respirer(self):
        print(f"{self.nom} respire.")
    def manger(self):
        print(f"{self.nom} mange.")
    def boire(self):
        print(f"{self.nom} bouge.")

toby = Giraffe("Toby", 100, 1000, 2.5) # Création d'un objet de type Giraffe
toby.respirer() # Appel de la méthode respirer() de l'objet toby
toby.manger() # Appel de la méthode manger() de l'objet toby
toby.boire() # Appel de la méthode boire() de l'objet toby

print("---")

yan = Giraffe("Yan", 200, 2000, 3.5) # Création d'un objet de type Giraffe
yan.respirer() # Appel de la méthode respirer() de l'objet yan
yan.manger() # Appel de la méthode manger() de l'objet yan
yan.boire() # Appel de la méthode boire() de l'objet yan