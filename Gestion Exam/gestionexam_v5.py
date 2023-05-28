import os
import datetime
import hashlib

class QCM:
    def __init__(self, numero_qcm, duree, questions):
        self.numero_qcm = numero_qcm
        self.duree = duree
        self.questions = questions

    def enregistrer(self):
        filename = f"QCM{self.numero_qcm}_{datetime.datetime.now().year}.txt"
        with open(filename, "w") as file:
            file.write(f"Numéro du QCM : {self.numero_qcm}\n")
            file.write(f"Durée du QCM : {self.duree}\n")
            file.write("Questions :\n")
            for i, question in enumerate(self.questions):
                file.write(f"{i+1}. {question['question']}\n")
                for j, reponse in enumerate(question['reponses']):
                    if j == question['reponse']:
                        file.write(f"-> {reponse}\n")
                    else:
                        file.write(f"-x {reponse}\n")

class Eleve:
    def __init__(self, nom_utilisateur, mot_de_passe):
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe

    def creer_compte(self):
        hashed_password = hashlib.sha256(self.mot_de_passe.encode()).hexdigest()
        filename = f"{self.nom_utilisateur.lower()}.txt"
        with open(filename, "w") as file:
            file.write(f"Nom d'utilisateur : {self.nom_utilisateur}\n")
            file.write(f"Mot de passe : {hashed_password}\n")

class Professeur:
    def __init__(self):
        self.qcms = []
        self.eleves = []
        for filename in os.listdir("."):
            if filename.endswith(".txt") and not filename.startswith("eleve_"):
                if filename.startswith("QCM"):
                    with open(filename, "r") as file:
                        lines = file.readlines()
                        numero_qcm = lines[0].split(": ")[1].strip()
                        duree = lines[1].split(": ")[1].strip()
                        questions = []
                        for i in range(3, len(lines)):
                            if lines[i].startswith("-x"):
                                reponse = lines[i][3:].strip()
                                questions[-1]['reponses'].append(reponse)
                            elif lines[i].startswith("->"):
                                reponse = lines[i][3:].strip()
                                questions[-1]['reponses'].append(reponse)
                                questions[-1]['reponse'] = len(questions[-1]['reponses']) - 1
                            else:
                                question = lines[i].strip()
                                questions.append({'question': question, 'reponses': [], 'reponse': None})
                        qcm = QCM(numero_qcm, duree, questions)
                        self.qcms.append(qcm)
                else:
                    with open(filename, "r") as file:
                        lines = file.readlines()
                        nom_utilisateur = lines[0].split(": ")[1].strip()
                        hashed_password = lines[1].split(": ")[1].strip()
                        eleve = Eleve(nom_utilisateur, hashed_password)
                        self.eleves.append(eleve)

    def menu(self):
        ActionForm({
            'c': ('Créer un QCM', self.creer_qcm),
            'a': ('Créer un compte élève', self.creer_compte_eleve),
            'crt': ('Corriger les réponses d\'un élève', self.correction_eleve),
            'r': ('Retour', None),
            'q': ('Quitter', self.quitter)
        })

    def creer_qcm(self):
        numero_qcm = input("Numéro du QCM : ")
        duree = input("Durée du QCM : ")
        questions = []
        while True:
            question = input("Question (ou 'q' pour quitter) : ")
class Professeur:
    def __init__(self):
        self.qcms = []
        self.eleves = []

    def menu(self):
        ActionForm({
            '1': ('Créer un QCM', self.creer_qcm),
            '2': ('Créer un compte élève', self.creer_compte_eleve),
            '3': ('Corriger un QCM', self.correction_eleve),
            'q': ('Quitter', self.quitter)
        })

    def creer_qcm(self):
        numero_qcm = input("Numéro du QCM : ")
        duree = input("Durée du QCM (en minutes) : ")
        nom_qcm = input("Nom du QCM : ")
        questions = []
        while True:
            question = input("Question (ou 'q' pour quitter) : ")
            if question == 'q':
                break
            reponses = []
            for i in range(4):
                reponse = input(f"Réponse {i+1} : ")
                reponses.append(reponse)
            bonne_reponse = int(input("Numéro de la bonne réponse : ")) - 1
            questions.append({'question': question, 'reponses': reponses, 'reponse': bonne_reponse})
        qcm = QCM(numero_qcm, duree, questions, nom_qcm)
        self.qcms.append(qcm)
        qcm.enregistrer()

    def creer_compte_eleve(self):
        nom_utilisateur = input("Nom d'utilisateur : ")
        mot_de_passe = input("Mot de passe : ")
        eleve = Eleve(nom_utilisateur, mot_de_passe)
        self.eleves.append(eleve)
        eleve.creer_compte()

    def correction_eleve(self):
        nom_utilisateur = input("Nom d'utilisateur de l'élève : ")
        qcm = self.choisir_qcm()
        filename = f"{nom_utilisateur}_{qcm.numero_qcm}_{datetime.datetime.now().year}.txt"
        with open(filename, "r") as file:
            reponses = file.readlines()
        score = 0
        for i, question in enumerate(qcm.questions):
            print(f"Question {i+1} : {question['question']}")
            for j, reponse in enumerate(question['reponses']):
                if j == question['reponse']:
                    print(f"-> {reponse}")
                else:
                    print(f"-x {reponse}")
            reponse_eleve = input("Réponse (1, 2, 3 ou 4) : ")
            while reponse_eleve not in ['1', '2', '3', '4']:
                print("Réponse invalide. Veuillez entrer 1, 2, 3 ou 4.")
                reponse_eleve = input("Réponse (1, 2, 3 ou 4) : ")
            if int(reponse_eleve) == question['reponse'] + 1:
                score += 1
        print(f"Score : {score}/{len(qcm.questions)}")

    def choisir_qcm(self):
        print("QCMs disponibles :")
        for i, qcm in enumerate(self.qcms):
            print(f"{i+1}. {qcm.nom_qcm}")
        choix = int(input("Numéro du QCM : ")) - 1
        return self.qcms[choix]

    def quitter(self):
        print("\033c")
        exit()

class MenuEleve:
    def __init__(self, professeur):
        self.professeur = professeur

    def menu(self):
        print("Nom d'utilisateur : ", end="")
        nom_utilisateur = input()
        print("Mot de passe : ", end="")
        mot_de_passe = hashlib.sha256(input().encode()).hexdigest()
        print(f"\033[2mdebug : nom_utilisateur (envoyé) : {nom_utilisateur}\033[0m")
        print(f"\033[2mdebug : mot_de_passe (envoyé) : {mot_de_passe}\033[0m")
        
        eleve = self.trouver_eleve(nom_utilisateur, mot_de_passe)

        if eleve is None:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            return
        qcms = self.trouver_qcms(eleve)
        if len(qcms) == 0:
            print("Aucun QCM disponible.")
            return
        print("QCMs disponibles :")
        for i, qcm in enumerate(qcms):
            print(f"{i+1}. {qcm.nom_qcm}")
        choix = int(input("Numéro du QCM : ")) - 1
        qcm = qcms[choix]
        filename = f"{eleve.nom_utilisateur}_{qcm.numero_qcm}_{datetime.datetime.now().year}.txt"
        if os.path.exists(filename):
            print("Vous avez déjà répondu à ce QCM.")
            return
        with open(filename, "w") as file:
            for i, question in enumerate(qcm.questions):
                print(f"Question {i+1} : {question['question']}")
                for j, reponse in enumerate(question['reponses']):
                    print(f"{j+1}. {reponse}")
                reponse = input("Réponse (1, 2, 3 ou 4) : ")
                while reponse not in ['1', '2', '3', '4']:
                    print("Réponse invalide. Veuillez entrer 1, 2, 3 ou 4.")
                    reponse = input("Réponse (1, 2, 3 ou 4) : ")
                file.write(f"{reponse}\n")
        print("QCM enregistré.")

    def trouver_eleve(self, nom_utilisateur, mot_de_passe):
        print(f"\033[2mdebug : nom_utilisateur (recu) : {nom_utilisateur}\033[0m")
        print(f"\033[2mdebug : mot_de_passe (recu) : {mot_de_passe}\033[0m")

        print(f"\033[2mdebug : all eleves : ")
        print(self.professeur.eleves)
        for eleve in self.professeur.eleves:
            print(eleve.nom_utilisateur, eleve.mot_de_passe)
        print("\033[0m")
        for eleve in self.professeur.eleves:
            print(f"\033[2mdebug : existing hash : {eleve.mot_de_passe}\033[0m")
            print(f"\033[2mdebug : correct : {eleve.mot_de_passe == mot_de_passe}\033[0m")
            if eleve.nom_utilisateur == nom_utilisateur and eleve.mot_de_passe == mot_de_passe:
                return eleve
        return None

    def trouver_qcms(self, eleve):
        qcms = []
        for qcm in self.professeur.qcms:
            filename = f"{eleve.nom_utilisateur}_{qcm.numero_qcm}_{datetime.datetime.now().year}.txt"
            if not os.path.exists(filename):
                qcms.append(qcm)
        return qcms

def ActionForm(actions):
    while True:
        print("Veuillez choisir une option : (", end="")
        for key in actions:
            print(f"'{key}': {actions[key][0]}", end=", ")
        print("\b\b)")

        choice = input("Action: ").lower()
        if choice in actions:
            if actions[choice][1] is not None:
                actions[choice][1]()
            return choice
        else:
            print("\033[95mErreur: choix invalide. Veuillez réessayer.\033[0m")

def main():
    professeur = Professeur()
    while True:
        ActionForm({
            'p': ('Mode Professeur', professeur.menu),
            'e': ('Mode Élève', MenuEleve(professeur).menu),
            'q': ('Quitter', professeur.quitter)
        })

if __name__ == '__main__':
    main()
    