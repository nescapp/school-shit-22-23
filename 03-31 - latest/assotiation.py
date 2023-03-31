# make a basic association between two objects

class Employe:
    """classe de base pour les employes"""
    def __init__(self, nom_de_l_employe, age_de_l_employe):
        self.nom_de_l_employe = nom_de_l_employe
        self.age_de_l_employe = age_de_l_employe

    def change_name(self, new_name):
        self.nom_de_l_employe = new_name

    def change_age(self, new_age):
        self.age_de_l_employe = new_age

    # def __repr__(self):
    #     return "%s %s" % (self.nom_de_l_employe, self.age_de_l_employe)


class Society:
    """classe de base pour les societes"""
    def __init__(self):
        self.employes = []
        self.nom_de_la_societe = "Carrefour"
        self.date_de_creation = "01/01/2000"

    def add(self, nom_de_l_employe, age_de_l_employe):
        self.employes.append(Employe(nom_de_l_employe, age_de_l_employe))

    def __repr__(self):
        return str(self.employes)

if __name__ == "__main__":
    # creation de la societe
    carrefour = Society()
    # ajout d'employes
    carrefour.add("John", 21)
    carrefour.add("Jack", 22)
    carrefour.add("Jill", 23)
    carrefour.add("Jane", 24)
    carrefour.add("Joe", 25)
    # modification d'un employe
    carrefour.employes[0].change_name("Karl")
    carrefour.employes[0].change_age(26)

    # affichage des informations de la societe
    print(f"La societe \033[92m{carrefour.nom_de_la_societe}\033[0m a ete cree le \033[92m{carrefour.date_de_creation}\033[0m et compte \033[92m{len(carrefour.employes)}\033[0m employes.")
    print("\n\033[4mListe des employes:\033[0m")
    
    for employe in carrefour.employes:
        # affichage les employes avec un formatage
        print(f"\033[2m {carrefour.employes.index(employe)+1:02}| Nom: \033[0m{employe.nom_de_l_employe}\033[2m \tAge: \033[0m{employe.age_de_l_employe}")