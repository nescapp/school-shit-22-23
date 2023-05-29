import datetime
import json
import os
import getpass
import msvcrt
import hashlib
import logging

"""
Modules utilisés:
datetime: pour la gestion de la date
json: pour la gestion du fichier users.json
os: pour la gestion du chemin du fichier users.json
getpass et msvcrt: pour cacher le mot de passe de l'utilisateur lors de la saisie dans la CLI
hashlib: pour hasher le mot de passe de l'utilisateur en SHA256
logging: pour enregistrer les activités de l'utilisateur dans un fichier log
"""

class QCM:
    def __init__(self, numero_qcm, nombre_questions, duree):
        self.numero_qcm = numero_qcm
        self.nombre_questions = nombre_questions
        self.duree = duree
        self.questions = []

    def ajouter_question(self, question, reponses, reponse_correcte):
        self.questions.append((question, reponses, reponse_correcte))

    def enregistrer_qcm(self):
        nom_fichier = f"QCM{self.numero_qcm}.txt"
        with open(nom_fichier, "w") as fichier:
            fichier.write(f"Numéro du QCM : {self.numero_qcm}\n")
            fichier.write(f"Nombre de questions : {self.nombre_questions}\n")
            fichier.write(f"Durée : {self.duree} minutes\n")
            fichier.write("\n")
            for i, (question, reponses, reponse_correcte) in enumerate(self.questions, start=1):
                fichier.write(f"Question {i}: {question}\n")
                for j, reponse in enumerate(reponses, start=1):
                    fichier.write(f"   {j}. {reponse}\n")
                fichier.write(f"   -> Réponse correcte : {reponse_correcte}\n")
                fichier.write("\n")

    def charger_qcm(self, numero_qcm):
        nom_fichier = f"QCM{numero_qcm}.txt"
        with open(nom_fichier, "r") as fichier:
            # Charger les informations du QCM à partir du fichier texte
            pass


class Eleve:
    def __init__(self, nom, numero_inscription, annee_naissance):
        self.nom = nom
        self.numero_inscription = numero_inscription
        self.annee_naissance = annee_naissance

    def creer_compte(self):
        nom_fichier = f"{self.nom}_{self.numero_inscription}.txt"
        with open("eleves.txt", "a") as fichier:
            fichier.write(f"Nom : {self.nom}\n")
            fichier.write(f"Numéro d'inscription : {self.numero_inscription}\n")
            fichier.write(f"Année de naissance : {self.annee_naissance}\n")
            fichier.write("\n")
        with open(nom_fichier, "w") as fichier:
            pass

    def passer_test(self):
        # Afficher la liste des QCM non encore effectués
        qcms_non_effectues = self.obtenir_qcms_non_effectues()
        if len(qcms_non_effectues) == 0:
            print("Aucun QCM disponible.")
            return

        # L'élève choisit un QCM
        print("Liste des QCM disponibles :")
        for i, qcm in enumerate(qcms_non_effectues, start=1):
            print(f"{i}. QCM {qcm.numero_qcm}")
        choix = input("Veuillez choisir un QCM : ")
        if not choix.isdigit() or int(choix) < 1 or int(choix) > len(qcms_non_effectues):
            print("Choix invalide.")
            return

        qcm_choisi = qcms_non_effectues[int(choix) - 1]
        reponses = self.repondre_questions(qcm_choisi)
        self.enregistrer_test(qcm_choisi, reponses)

    def obtenir_qcms_non_effectues(self):
        # Charger les QCMs non encore effectués
        qcms_non_effectues = []
        for numero_qcm in range(1, 4):  # Exemple avec 3 QCMs
            nom_fichier = f"QCM{numero_qcm}.txt"
            if not self.qcm_effectue(nom_fichier):
                qcm = QCM(numero_qcm, 0, 0)
                qcm.charger_qcm(numero_qcm)
                qcms_non_effectues.append(qcm)
        return qcms_non_effectues

    def qcm_effectue(self, nom_fichier):
        # Vérifier si l'élève a déjà effectué le QCM en examinant son fichier associé
        return False  # À compléter

    def repondre_questions(self, qcm):
        reponses = []
        for i, (question, reponses, _) in enumerate(qcm.questions, start=1):
            print(f"Question {i}: {question}")
            for j, reponse in enumerate(reponses, start=1):
                print(f"   {j}. {reponse}")
            choix = input("Veuillez choisir une réponse : ")
            if not choix.isdigit() or int(choix) < 1 or int(choix) > len(reponses):
                print("Choix invalide.")
                return []
            reponses.append(int(choix))
        return reponses

    def enregistrer_test(self, qcm, reponses):
        nom_fichier = f"{self.nom}_{self.numero_inscription}.txt"
        with open(nom_fichier, "a") as fichier:
            fichier.write(f"QCM : {qcm.numero_qcm}\n")
            fichier.write(f"Date du test : {datetime.date.today()}\n")
            fichier.write(f"Durée du test : {qcm.duree} minutes\n")
            fichier.write("Réponses :\n")
            for i, reponse in enumerate(reponses, start=1):
                fichier.write(f"Question {i}: {reponse}\n")
            fichier.write("\n")

    def evaluer_test(self):
        nom_fichier = f"{self.nom}_{self.numero_inscription}.txt"
        with open(nom_fichier, "r") as fichier:
            # Évaluer le test de l'élève et afficher les résultats
            pass


class Professeur:
    def __init__(self, nom):
        self.nom = nom

    def creer_qcm(self):
        numero_qcm = int(input("Numéro du QCM : "))
        nombre_questions = int(input("Nombre de questions : "))
        duree = int(input("Durée du QCM en minutes : "))

        qcm = QCM(numero_qcm, nombre_questions, duree)

        for i in range(nombre_questions):
            question = input(f"Question {i + 1} : ")
            reponses = []
            for j in range(4):
                reponse = input(f"Réponse {j + 1} : ")
                reponses.append(reponse)
            reponse_correcte = int(input("Numéro de la réponse correcte : "))
            qcm.ajouter_question(question, reponses, reponse_correcte)

        qcm.enregistrer_qcm()

    def ajouter_eleve(self, eleve):
        eleve.creer_compte()

    def evaluer_tests(self):
        eleves = self.charger_eleves()
        for eleve in eleves:
            eleve.evaluer_test()

    def charger_eleves(self):
        eleves = []
        with open("eleves.txt", "r") as fichier:
            # Charger les informations des élèves à partir du fichier texte
            pass
        return eleves


def menu_principal():
    print("----- Menu Principal -----")
    print("1. Mode Professeur")
    print("2. Mode Élève")
    print("0. Quitter")


def menu_professeur():
    print("----- Mode Professeur -----")
    print("1. Créer un QCM")
    print("2. Ajouter un élève")
    print("3. Évaluer les tests")
    print("0. Retour")


def menu_eleve():
    print("----- Mode Élève -----")
    print("1. Passer un test")
    print("2. Évaluation d'un test")
    print("0. Retour")


def main():
    while True:
        menu_principal()
        choix = input("Veuillez choisir une option : ")
        if choix == "1":
            mode_professeur()
        elif choix == "2":
            mode_eleve()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")


def mode_professeur():
    professeur = Professeur("Professeur")
    while True:
        menu_professeur()
        choix = input("Veuillez choisir une option : ")
        if choix == "1":
            professeur.creer_qcm()
        elif choix == "2":
            nom = input("Nom de l'élève : ")
            numero_inscription = input("Numéro d'inscription : ")
            annee_naissance = input("Année de naissance : ")
            eleve = Eleve(nom, numero_inscription, annee_naissance)
            professeur.ajouter_eleve(eleve)
        elif choix == "3":
            professeur.evaluer_tests()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")


def mode_eleve():
    nom = input("Nom de l'élève : ")
    numero_inscription = input("Numéro d'inscription : ")
    eleve = Eleve(nom, numero_inscription, 0)
    while True:
        menu_eleve()
        choix = input("Veuillez choisir une option : ")
        if choix == "1":
            eleve.passer_test()
        elif choix == "2":
            eleve.evaluer_test()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()