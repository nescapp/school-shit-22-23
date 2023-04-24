class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.tfe = None
    
    def realiser_tfe(self, tfe):
        self.tfe = tfe
        
    def obtenir_note_tfe(self):
        return self.tfe.note if self.tfe else 0

class TFE:
    def __init__(self, titre, professeur):
        self.titre = titre
        self.professeur = professeur
        self.etudiants = []
        self.note = None
        
    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
    
    def enregistrer_note(self, note):
        self.note = note
        
class Professeur:
    def __init__(self, nom):
        self.nom = nom
        self.tfes_encadres = []
        
    def encadrer_tfe(self, tfe):
        self.tfes_encadres.append(tfe)

def valider_diplomes(etudiants):
    for etudiant in etudiants:
        if etudiant.tfe and etudiant.obtenir_note_tfe() >= 12:
            print(f"{etudiant.nom} a validé son diplôme !")
        else:
            print(f"{etudiant.nom} n'a pas validé son diplôme.")

# Création des professeurs
prof1 = Professeur("Dupont")
prof2 = Professeur("Martin")

# Création des TFEs
tfe1 = TFE("Titre 1", prof1)
tfe2 = TFE("Titre 2", prof2)

# Ajout des étudiants aux TFEs
etudiant1 = Etudiant("Jean")
etudiant2 = Etudiant("Marie")
tfe1.ajouter_etudiant(etudiant1)
tfe1.ajouter_etudiant(etudiant2)

etudiant3 = Etudiant("Pierre")
tfe2.ajouter_etudiant(etudiant3)

# Encadrement des TFEs par les professeurs
prof1.encadrer_tfe(tfe1)
prof2.encadrer_tfe(tfe2)

# Enregistrement des notes des TFEs
tfe1.enregistrer_note(14)
tfe2.enregistrer_note(10)

# Validation des diplômes
etudiants = [etudiant1, etudiant2, etudiant3]
valider_diplomes(etudiants)
