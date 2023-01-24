class Moto:
    def __init__(self, marque, prix, puissance):
        self.marque = marque
        self.prix = prix
        self.puissance = puissance

    def __str__(self):
        return f"{self.marque}, {self.prix}, {self.puissance}"

    def get_marque(self):
        return self.marque
    def get_prix(self):
        return self.prix
    def get_puissance(self):
        return self.puissance

    def set_marque(self, marque, a):
        self.marque = a
    def set_prix(self, prix, a):
        self.prix = a
    def set_puissance(self, puissance, a):
        self.puissance = a   

catalogue = [
    ["KTM", 5_000, 15],
    ["Hama", 10_000, 11],
    ["Honda", 6_500, 12],
    ]
for moto in catalogue:
    moto = Moto(moto[0], f'{moto[1]:_}', moto[2])
    print(moto)

moto.set_marque(moto.get_marque(), "Yamaha")
moto.set_prix(moto.get_prix(), 7_000)
moto.set_puissance(moto.get_puissance(), 13)
print(moto)
