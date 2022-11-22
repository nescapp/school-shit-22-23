class Fleurs:
    def __init__(self, couleur, prix):
        self.couleur = couleur
        self.prix = prix

        print(f"{self.couleur} : {self.prix}€")

Fleur1 = Fleurs("Tulipe", 1.5)
Fleur2 = Fleurs("Rose", 2.5)