class Moto:
    def __init__(self, marque, prix, puissance):
        self.marque = marque
        self.prix = prix
        self.puissance = puissance

    def __str__(self):
        return f"{self.marque}, {self.prix}, {self.puissance}"

catalogue = [
    ["KTM", 5_000, 15],
    ["Hama", 10_000, 11],
    ["Honda", 6_500, 12],
    ]
for moto in catalogue:
    moto = Moto(moto[0], f'{moto[1]:_}', moto[2])
    
    print(moto)
