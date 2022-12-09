class Giraffe:
    def __init__(self, taches, poids, taille):
        self.taches = taches
        self.poids = poids
        self.taille = taille
        print("Je suis une girafe")

    def respirer(self):
        print("Je respire")
    def manger(self):
        print("Je mange")
    def boire(self):
        print("Je bouge")

toby = Giraffe(100, 1000, 2.5)
toby.respirer()
toby.manger()
toby.boire()

print("---")

yan = Giraffe(200, 2000, 3.5)
yan.respirer()
yan.manger()
yan.boire()