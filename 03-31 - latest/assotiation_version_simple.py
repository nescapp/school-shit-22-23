class Employe:
    
    def __init__(self, nom_employe, age_employe):
        self.nom_employe = nom_employe
        self.age_employe = age_employe

    def change_name(self, new_name):
        self.nom_employe = new_name

    def change_age(self, new_age):
        self.age_employe = new_age


class Society:
    
    def __init__(self):
        self.employes = []
        self.nom_societe = "Carrefour"
        self.date_creation = "01/01/2000"

    def add(self, nom_employe, age_employe):
        self.employes.append(Employe(nom_employe, age_employe))

    def __repr__(self):
        return str(self.employes)

if __name__ == "__main__":
    
    carrefour = Society()
    
    carrefour.add("John", 21) 
    carrefour.add("Jack", 22)
    carrefour.add("Jill", 23)
    carrefour.add("Jane", 24)
    carrefour.add("Joe", 25)
    
    carrefour.employes[0].change_name("Karl")
    carrefour.employes[0].change_age(26)

    
    print(f"La societe {carrefour.nom_societe} a ete cree le {carrefour.date_creation} et compte {len(carrefour.employes)} employes.")
    print("\nListe des employes:")
    
    for employe in carrefour.employes:
        
        print(f" {carrefour.employes.index(employe)+1:02}| Nom: {employe.nom_employe} Age: {employe.age_employe}")
