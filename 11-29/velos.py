""" Consignes :
- Créer une classe Velos.
- Créer 2 instances de la classe Vélos: velo1, velo2, 

Dans la classe Velos :
- Déclarer et initialiser via  le constructeur les 3  attributs suivants  : marque, prix, couleur.
- Créer une fonction Deplacer() permettant de déplacer velo1 de manière à ce qu'il forme un carré et qu'il puisse revenir à la case de départ.
- Pour cela importer pour cela le module turtle.
- Appeler la fonction Pen() permettant le déplacement de l'objet velo1.
- Pour cela, créer un nouveau canevas(une interface graphique) en appliquant l'instruction suivante :
          velo1=turtle.Pen()

- Pour déplacer velo1 tu fais appel à des fonctions disponibles dans la variable velo1.

 Par exemple, pour dire à velo1 d'avancer de 50 mètres(pixels), tu tapes l'instruction suivante :

velo1.forward(50).

Les autres instructions à vous de les découvrir !

- Afficher les attributs des 2 instances dans le programme principal. """
import turtle

class Velos:
    def __init__(self, marque:str, prix:float, couleur:str):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur

def Deplacer(target):
    """permettant de déplacer velo1 de manière à ce qu'il forme un carré et qu'il puisse revenir à la case de départ"""
    target.forward(50)


velo1 = Velos("a", 1, "bleu")
velo2 = Velos("b", 2, "rouge")

# create a new canvas
velo1=turtle.Pen()

# move forward
Deplacer(velo1)
# leave the window open until the user clicks on it
turtle.mainloop()


