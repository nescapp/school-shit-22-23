import random # Importation du module random

class BoulesDePetanque:
    """Classe permettant de créer des boules de pétanque"""
    def __init__(self, player):
        # Définition des attributs
        if player == "tireur":
            self.poids = random.randint(670, 700)
        elif player == "pointeur":
            self.poids = random.randint(710, 730)
        elif player == "milieu":
            self.poids = random.randint(680, 720)

        self.player = player
        self.diametre = random.randint(13, 76)
        self.volume = 4/3 * 3.14 * (self.diametre/2)**3
        self.densite = 0.0027
        self.masse = self.densite * self.volume
    
    # Définition des méthodes get et set
    def get_player(self):
        return self.player
    def get_poids(self):
        return self.poids
    def get_volume(self):
        return self.volume
    def get_diametre(self):
        return self.diametre
    def get_densite(self):
        return self.densite
    def get_masse(self):
        return self.masse

    def set_poids(self, value):
        self.poids = value
        print(f"    Le poids a été modifié à {self.poids} g\n")
    def set_volume(self, value):
        self.volume = value
        print(f"    Le volume a été modifié à {self.volume} cm3\n")
    def set_diametre(self, value):
        self.diametre = value
        print(f"    Le diamètre a été modifié à {self.diametre} mm\n")
    def set_densite(self, value):
        self.densite = value
        print(f"    La densité a été modifiée à {self.densite} kg/cm3\n")
    def set_masse(self, value):
        self.masse = value
        print(f"    La masse a été modifiée à {self.masse} kg\n")

    # Définition de la méthode __str__ pour afficher les informations de la boule
    def __str__(self):
        return f"""
    Il s'agit d'une boule de pétanque pour le joueur {self.player},
    Le poids de la boule est de {self.poids} g,
    Le volume de la boule est de {self.volume} cm3,
    Le diamètre de la boule est de {self.diametre} mm,
    La densité de la boule est de {self.densite} kg/cm3,
    La masse de la boule est de {self.masse} kg
        """

# Création des boules de pétanque
print("\033[94mCréation des boules de pétanque pour le joueur 1\033[0m")
boule1 = BoulesDePetanque("tireur")
print(boule1)
print("\033[94mCréation des boules de pétanque pour le joueur 2\033[0m")
boule2 = BoulesDePetanque("milieu")
print(boule2)
print("\033[94mCréation des boules de pétanque pour le joueur 3\033[0m")
boule3 = BoulesDePetanque("pointeur")
print(boule3)

# Modification du poids de la boule 1
print("\033[94mModification du poids de la boule 1\033[0m")
boule1.set_poids(680)