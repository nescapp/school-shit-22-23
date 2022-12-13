class Papillion: # classe
    def __init__(self, nom, pondDesOeufs, poids, taille): # constructeur
        self.nom = nom # attribut
        self.pondDesOeufs = pondDesOeufs # attribut
        self.poids = poids # attribut
        self.taille = taille # attribut

    def respier(self): # methode
        return f"{self.nom} respire" # retourne une chaine de caractere

    def manger(self): # methode
        return f"{self.nom} mange" # retourne une chaine de caractere

    def voler(self): # methode
        return f"{self.nom} vole" # retourne une chaine de caractere


fleur = Papillion("fleur", 150, 0.3, 5.70) # objet
nuage = Papillion("nuage", 2500, 0.5, 7.70) # objet

print(fleur.respier()) # appel de la methode respier de l'objet fleur
print(fleur.manger()) # appel de la methode manger de l'objet fleur
print(fleur.voler()) # appel de la methode bouger de l'objet fleur
print()
print(nuage.respier()) # appel de la methode respier de l'objet nuage
print(nuage.manger()) # appel de la methode manger de l'objet nuage
print(nuage.voler()) # appel de la methode bouger de l'objet nuage