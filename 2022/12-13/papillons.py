class Papillon:
    """Classe représentant un papillon."""
    def __init__(self, nom:str, oeufs:int, poids:float, taille:int):
        # Attributs d'instance
        self.nom = nom
        self.oeufs = oeufs
        self.poids = poids
        self.taille = taille
        print(f"{self.nom} est un Papillon.") # Affiche un message de création
        print(f"{self.nom} pond {self.oeufs} oeufs.")
        print(f"{self.nom} pèse {self.poids} grammes.")
        print(f"{self.nom} mesure {self.taille} cm.")

    def respirer(self):
        print(f"{self.nom} respire.")
    def manger(self, nourriture):
        print(f"{self.nom} mange {nourriture}.")
    def voler(self):
        print(f"{self.nom} vole.")

fleur = Papillon("Fleur", 50, 0.3, 11) # Création d'un objet de type Papillon
fleur.respirer() # Appel de la méthode respirer() de l'objet fleur
fleur.manger("des fleurs") # Appel de la méthode manger() de l'objet fleur
fleur.voler() # Appel de la méthode voler() de l'objet fleur

print("---")

nuage = Papillon("Nuage", 100, 0.5, 12) # Création d'un objet de type Papillon
nuage.respirer() # Appel de la méthode respirer() de l'objet nuage
nuage.manger("des fleurs") # Appel de la méthode manger() de l'objet nuage
nuage.voler() # Appel de la méthode voler() de l'objet nuage
