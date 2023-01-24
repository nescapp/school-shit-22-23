class Facture:
    compteurFacture = 0
    def __init__(self, date, client, articles, brut, net, tva):
        Facture.compteurFacture += 1
        self.date = date
        self.client = client
        self.articles = articles
        self.brut = brut
        self.net = brut - brut * 0.2
        self.tva = brut * 0.2

    def get_date(self):
        return self.date
    def get_client(self):
        return self.client
    def get_articles(self):
        return self.articles
    def get_brut(self):
        return self.brut
    def get_net(self):
        return self.net
    def get_tva(self):
        return self.tva

    def set_date(self, date, a):
        self.date = a
    def set_client(self, client, a):
        self.client = a
    def set_articles(self, articles, a):
        self.articles = a
    def set_brut(self, brut, a):
        self.brut = a
    def set_net(self, net, a):
        self.net = a
    def set_tva(self, tva, a):
        self.tva = a

    def __str__(self):
        return "Facture du " + str(self.date) + " pour " + str(self.client) + " avec " + str(self.articles) + " pour un montant de " + str(self.brut) + " euros." + " TVA: " + str(self.tva) + " euros. Net: " + str(self.net) + " euros."


facture1 = Facture("01/01/2020", "Jean", ["Brocoli", "Mandarine"], 10, 8, 2)
facture2 = Facture("02/01/2020", "Pierre", ["Jus d'orange", "Pain", "Chips"], 15, 12, 3)
facture3 = Facture("03/01/2020", "Paul", ["Chocolat", "Chips", "Coca", "Pain"], 20, 16, 4)
facture4 = Facture("04/01/2020", "Jacques", ["Chocolat", "Chips", "Coca", "Pain"], 20, 16, 4)

facture1.set_date(facture1, "01/01/2020")
facture1.set_client(facture1, "Jean")
facture1.set_articles(facture1, ["Brocoli", "Mandarine"])
facture1.set_brut(facture1, 20)
facture1.set_net(facture1, 16)
facture1.set_tva(facture1, 4)

facture2.set_date(facture2, "02/01/2020")
facture2.set_client(facture2, "Pierre")
facture2.set_articles(facture2, ["Jus d'orange", "Pain", "Chips"])
facture2.set_brut(facture2, 30)
facture2.set_net(facture2, 24)
facture2.set_tva(facture2, 6)

facture3.set_date(facture3, "03/01/2020")
facture3.set_client(facture3, "Paul")
facture3.set_articles(facture3, ["Chocolat", "Chips", "Coca", "Pain"])
facture3.set_brut(facture3, 40)
facture3.set_net(facture3, 32)
facture3.set_tva(facture3, 8)

facture4.set_date(facture4, "04/01/2020")
facture4.set_client(facture4, "Jacques")
facture4.set_articles(facture4, ["Chocolat", "Chips", "Coca", "Pain"])
facture4.set_brut(facture4, 40)
facture4.set_net(facture4, 32)
facture4.set_tva(facture4, 8)




print(facture1, "\n")
print(facture2, "\n")
print(facture3, "\n")
print("\033[96mNombre de factures: " + str(Facture.compteurFacture) + "\033[0m")
