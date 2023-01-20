class Facture:
    compteurFacture = 0
    def __init__(self, date, client, articles, brut):
        Facture.compteurFacture += 1
        self.date = date
        self.client = client
        self.articles = articles
        self.brut = brut
        self.net = brut - brut * 0.2
        self.tva = brut * 0.2
    
    def __str__(self):
        return "Facture du " + str(self.date) + " pour " + str(self.client) + " avec " + str(self.articles) + " pour un montant de " + str(self.brut) + " euros." + " TVA: " + str(self.tva) + " euros. Net: " + str(self.net) + " euros."

    
facture1 = Facture("01/01/2020", "Jean", ["Brocoli", "Mandarine"], 10)
facture2 = Facture("02/01/2020", "Pierre", ["Jus d'orange", "Pain", "Chips"], 15)
facture3 = Facture("03/01/2020", "Paul", ["Chocolat", "Chips", "Coca", "Pain"], 20)
facture4 = Facture("04/01/2020", "Jacques", ["Chocolat", "Chips", "Coca", "Pain"], 20)

print(facture1)
print(facture2)
print(facture3)
print("Nombre de factures: " + str(Facture.compteurFacture))
