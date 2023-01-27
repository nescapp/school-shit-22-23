import turtle
import time
class Velos:
    def __init__(self, marque:str, prix:float, couleur:str):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur

    def get_marque(self):
        return self.marque
    def get_prix(self):
        return self.prix
    def get_couleur(self):
        return self.couleur

    def set_marque(self, marque, a):
        self.marque = a
    def set_prix(self, prix, a):
        self.prix = a
    def set_couleur(self, couleur, a):
        self.couleur = a

def Deplacer(target_velo, color):
    time.sleep(0.5)
    target_velo.color(color)
    target_velo.forward(50)
    target_velo.left(90)
    target_velo.forward(50)
    target_velo.left(90)
    target_velo.forward(50)
    target_velo.left(90)
    target_velo.forward(50)
    target_velo.left(90)


velo1 = Velos("a", 1, "bleu")
velo2 = Velos("b", 2, "rouge")

velo1.set_marque(velo1.get_marque(), "Yamaha")
velo1.set_prix(velo1.get_prix(), 7_000)
velo1.set_couleur(velo1.get_couleur(), "jaune")

velo2.set_marque(velo2.get_marque(), "Kawasaki")
velo2.set_prix(velo2.get_prix(), 8_000)
velo2.set_couleur(velo2.get_couleur(), "vert")

print(f"vélo n°1 : {velo1.marque, velo1.prix, velo1.couleur}")
print(f"vélo n°2 : {velo2.marque, velo2.prix, velo2.couleur}")

velo1=turtle.Pen()
Deplacer(velo1, "blue")
velo2=turtle.Pen()
Deplacer(velo2, "red")

turtle.mainloop()