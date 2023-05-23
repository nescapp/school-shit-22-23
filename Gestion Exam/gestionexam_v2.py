import json
import os
import getpass
import msvcrt
import hashlib
import logging

"""
Modules utilisés:
json: pour la gestion du fichier users.json
os: pour la gestion du chemin du fichier users.json
getpass et msvcrt: pour cacher le mot de passe de l'utilisateur lors de la saisie dans la CLI
hashlib: pour hasher le mot de passe de l'utilisateur en SHA256
logging: pour enregistrer les activités de l'utilisateur dans un fichier log
"""

# variables globales
MODE = None
DB = os.path.join(os.path.dirname(__file__), "users.json")

"""
Vaiables globales:
DB: chemin du fichier users.json
users: dictionnaire qui contient les utilisateurs dans le fichier users.json
"""


class Utilisateur():
    def __init__(self, nom, prenom, nom_utilisateur, mot_de_passe_hash, type):
        self.nom = nom
        self.prenom = prenom
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe_hash = mot_de_passe_hash
        self.type = type
    
    def create_new(nom, prenom, nom_utilisateur, mot_de_passe_hash, type, verbose=True):
        pass

class Professeur(Utilisateur):
    def menu(self):
        # still working on it
        pass
    def create_qcm(self):
        # still working on it
        pass

class Eleve(Utilisateur):
    def menu(self):
        # still working on it
        pass
    def start_qcm(self):
        # still working on it
        pass
    def check_qcm(self):
        # still working on it
        pass

class QCM():
    def __init__(self, id, creation_date, duration):
        self.id = id
        self.creation_date = creation_date
        self.duration = duration

class Question(QCM):
    def __init__(self, id, question, options, answer):
        self.id = id
        self.question = question
        self.options = options
        self.answer = answer

# fonctions debug

def debugUserList():
    """Fonction qui permet d'afficher la liste des utilisateurs dans la CLI."""
    if os.stat(DB).st_size != 0:
        # Si le fichier n'est pas vide
        for user in users:
            # Afficher le nom d'utilisateur et le type
            print(f"{user} - ", end="")
            if users[user]["type"] == "e":
                print("\033[93mélève\033[0m")
            elif users[user]["type"] == "p":
                print("\033[94mprof\033[0m")
    else:
        print("\033[95maucun utilisateur n'existe\033[0m")
    MainMenuScreen()


def debugReset():
    """Fonction qui permet de réinitialiser le fichier users.json. Cette fonction est temporaire et sera supprimée dans la version finale."""
    global users

    

    with open(DB, "r") as file:
        users = json.load(file)
    logging.info("reset users successfully")
    print("\033[92mUtilisateurs réinitialisés avec succès.\033[0m")
    MainMenuScreen()


# écrans

def MainMenuScreen():
    """Fonction qui permet d'afficher le menu principal de l'utilisateur."""
    global mode
    print("définir le mode de gestion des examens: ")
    ActionForm(
        {
            "e": ("Mode élève", lambda: ConnectUserForm("e")),
            "p": ("Mode prof", lambda: ConnectUserForm("p")),
            "x": ("@debug Reset", lambda: debugReset()),
            "l": ("@debug Liste", lambda: debugUserList()),
            "q": ("Quitter", lambda: Quit()),
        }
    )


# fonctions porgamme

def SetMode(new_mode):
    """Fonction qui permet de définir le mode de l'utilisateur."""
    global mode
    mode = new_mode
    logging.info(f"mode set to {new_mode}")


def ActionForm(actions):
    """Fonction qui permet d'afficher un formulaire d'actions et d'exécuter l'action choisie par l'utilisateur."""
    while True:
        # afficher les actions
        print("(", end="")
        for key in actions:
            print(f"'{key}': {actions[key][0]}", end=", ")
            logging.info(f"actions: {key} - {actions[key][0]}")
        print("\b\b)")

        # saisir l'action
        choice = input("Action: ").lower()
        logging.info(f"input: {choice}")
        if choice in actions:
            # exécuter l'action choisie par l'utilisateur si elle existe
            actions[choice][1]()
            return choice
        else:
            print("\033[95merreur: choix invalide. Veuillez réessayer.\033[0m")


def Quit():
    """Fonction qui permet de quitter le programme."""
    logging.info("program quit")
    print("\033c")
    exit()


def init():
    """Fonction qui permet d'initialiser le programme."""
    global DB
    # configurer le logger
    LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "gestionexam.log")
    logging.basicConfig(filename=LOG, level=logging.INFO, format="%(asctime)s [info] %(message)s")
    logging.info("init started")
    # s'assurer que le dossier data existe (Il permet de stocker les fichiers de données du programme)
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")):
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
        logging.info("data folder created")
    # s'assurer que le fichier users.json existe
    if not os.path.exists(DB):
        open(DB, "w").close()
    else:
        # maintenant que le fichier existe, vérifier s'il est vide, si oui, créer le dictionnaire, sinon, trier les utilisateurs par type
        if os.stat(DB).st_size == 0:
            users = {}
        else:
            logging.info("starting to sort users")
            with open(DB, "r") as file:
                users = json.load(file)
            users = dict(
                sorted(users.items(), key=lambda item: item[1]["type"], reverse=True)
            )
            with open(DB, "w") as file:
                json.dump(users, file, indent=4)
            logging.info("sorted users successfully")

    logging.info("init ended")


def main():
    """Fonction principale du programme."""
    global mode
    # initialiser le programme
    init()
    # laisser l'utilisateur choisir son mode ('p' pour professeur, 'e' pour élève)
    print("Bienvenue dans le programme de gestion des examens. Choisissez votre mode:")





if __name__ == "__main__":
    # exécuter le programme si le fichier est exécuté directement
    main()