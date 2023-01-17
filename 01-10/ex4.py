class Facture:
    compteurFacture = 0
    def __init__(self, date, client, articles):
        Facture.compteurFacture += 1
        self.date = date
        self.client = client
        self.articles = articles
    
    def __str__(self):
        return "Facture du " + str(self.date) + " pour " + str(self.client) + " avec " + str(self.articles)

    
facture1 = Facture("01/01/2020", "Jean", ["Brocoli", "Mandarine"])
facture2 = Facture("02/01/2020", "Pierre", ["Jus d'orange", "Pain", "Chips"])
facture3 = Facture("03/01/2020", "Paul", ["Chocolat", "Chips", "Coca", "Pain"])

print(facture1)
print(facture2)
print(facture3)
print("Nombre de factures: " + str(Facture.compteurFacture))