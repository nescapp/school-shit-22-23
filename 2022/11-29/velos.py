import turtle
import time
class Velos:
    def __init__(self, marque:str, prix:float, couleur:str):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur

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

print(f"vélo n°1 : {velo1.marque, velo1.prix, velo1.couleur}")
print(f"vélo n°2 : {velo2.marque, velo2.prix, velo2.couleur}")

velo1=turtle.Pen()
Deplacer(velo1, "blue")
velo2=turtle.Pen()
Deplacer(velo2, "red")

turtle.mainloop()