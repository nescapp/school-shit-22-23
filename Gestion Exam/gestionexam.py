# importation des modules
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

def MenuProf():
    """Menu principal pour le mode professeur."""
    print("\033[2mdebug: menu prof\033[0m")
    ActionForm({"1": ("Créer un QCM", lambda: None),
                "2": ("Créer un compte élève", lambda: None),
                "3": ("Consulter les évaluations", lambda: None),
                "q": ("Quitter", lambda: Quit())})


def Quit():
    """Fonction qui permet de quitter le programme."""
    logging.info("program quit")
    print("\033c")
    exit()


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


def tempResetUsers():
    """Fonction qui permet de réinitialiser le fichier users.json. Cette fonction est temporaire et sera supprimée dans la version finale."""
    global users
    logging.info("resetting users initated")
    open(DB, "w").close()
    CreateNewUser("eleve", hashlib.sha256("eleve".encode()).hexdigest(), "e", False)
    logging.info("created user 'eleve'")
    CreateNewUser("prof", hashlib.sha256("prof".encode()).hexdigest(), "p", False)
    logging.info("created user 'prof'")
    # redefine users
    with open(DB, "r") as file:
        users = json.load(file)
    logging.info("reset users successfully")
    print("\033[92mUtilisateurs réinitialisés avec succès.\033[0m")

    DefineModeForm()


def UserList():
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
    
    DefineModeForm()  # retourner au menu principal


def Password():
    """Fonction qui permet de cacher le mot de passe de l'utilisateur lors de la saisie dans la CLI et de le hasher en SHA256 directement. Cette fonction retourne le mot de passe hashé et sa longueur."""
    password = ""
    length = 0
    print("\033[2m", end="")
    while True:
        last_char = msvcrt.getch().decode("utf-8")  # récupérer le dernier caractère
        if last_char == "\r" or last_char == "\n":
            # si l'utilisateur appuie sur entrée, sortir de la boucle
            print("\033[0m\n", end="")
            break
        elif last_char == "\b" and len(password) > 0:
            # si l'utilisateur appuie sur backspace, supprimer le dernier caractère
            password = password[:-1]
            length -= 1
            print("\b \b", end="", flush=True)
        elif last_char == "\b" and len(password) == 0:
            # si l'utilisateur appuie sur backspace et que le mot de passe est vide, rester dans la boucle
            continue
        else:
            # sinon ajouter le dernier caractère au mot de passe
            password += last_char
            length += 1
            print("*", end="", flush=True)

    # hasher le mot de passe en SHA256
    password = hashlib.sha256(password.encode()).hexdigest()
    return password, length


def VerifyUserExistance(username):
    """Function qui permet de vérifier si l'utilisateur existe déjà."""
    # vérifier si le fichier est vide
    if os.stat(DB).st_size != 0:
        # vérifier si l'utilisateur existe déjà
        with open(DB, "r") as file:
            users = json.load(file)
        if username in users:
            return True
        else:
            return False
    else:
        return False


def VerifyUserStatus(username):
    """Fonction qui permet de vérifier si l'utilisateur existe et si c'est un élève ou un prof."""
    # vérifier si le fichier est vide
    if os.stat(DB).st_size != 0:
        # vérifier si l'utilisateur existe déjà
        with open(DB, "r") as file:
            users = json.load(file)
        if username in users:
            if users[username]["type"] == "e":
                return "e"
            elif users[username]["type"] == "p":
                return "p"
            else:
                return False
        else:
            return False
    else:
        return False


def VerifyPassword(username, hash):
    """Fonction qui permet de vérifier si le mot de passe est correct en fournissant le nom d'utilisateur et le mot de passe à verifier hashé."""
    with open(DB, "r") as file:
        users = json.load(file)
    if username in users:
        if hash == users[username]["password"]:
            return True
        else:
            return False
    else:
        return False


def CreateNewUser(username, hash, type, verbose=True):
    # vérifier si le fichier est vide
    if os.stat(DB).st_size == 0:
        # si oui, créer le dictionnaire
        users = {}
    else:
        # vérifier si l'utilisateur existe déjà
        with open(DB, "r") as file:
            users = json.load(file)
        if username in users:
            print("\033[95merreur: ce nom d'utilisateur existe déjà\033[0m")
            return

    users[username] = {"password": hash, "type": type}

    with open(DB, "w") as file:
        json.dump(users, file, indent=4)

    if verbose:
        if type == "e":
            print(f"compte \033[93mélève '{username}'\033[0m créé avec succès")
        elif type == "p":
            print(f"compte \033[94mprof '{username}'\033[0m créé avec succès")


def ConnectUserForm(asmode):
    """Formulaire qui permet à l'utilisateur de se connecter à son compte ou de créer un compte."""
    print(f"\033[2mdebug: this is connect user form, asmode = {asmode}\033[0m")
    if asmode == "e":
        SetMode("e") # this is required because the DefineModeForm() can only call one function 
        print("connecter utilisateur \033[93mélève\033[0m")
    elif asmode == "p":
        SetMode("p")
        print("connecter utilisateur \033[94mprof\033[0m")

    ActionForm(
        {
            "l": ("Login", lambda: LoginForm(asmode)),
            "s": ("Signup", lambda: SignupForm(asmode)),
            "r": ("Retour", lambda: DefineModeForm()),
            "q": ("Quitter", lambda: Quit()),
        }
    )


def SetMode(mode):
    """Fonction qui permet de définir le mode de gestion des examens."""
    global current_mode
    if mode == "e":
        print("\033[93m[mode élève]\033[0m")
        current_mode = "e"
    elif mode == "p":
        print("\033[94m[mode prof]\033[0m")
        current_mode = "p"

    print(f"\033[2mdebug: current_mode = {current_mode}\033[0m")


def DefineModeForm():
    """Formulaire qui permet de définir le mode de gestion des examens selon l'utilisateur."""
    print("\033[2mdebug: this is define mode form\033[0m")
    print("définir le mode de gestion des examens: ")
    ActionForm(
        {
            "e": ("Mode élève", lambda: ConnectUserForm("e")),
            "p": ("Mode prof", lambda: ConnectUserForm("p")),
            "x": ("Reset", lambda: tempResetUsers()),
            "l": ("Liste", lambda: UserList()),
            "q": ("Quitter", lambda: Quit()),
        }
    )


def LoginForm(mode):
    """Formulaire de connexion à un compte."""
    global current_mode
    if current_mode == "e":
        print("\033[93m[se connecter à son compte élève]\033[0m")
    elif current_mode == "p":
        print("\033[94m[se connecter à son compte prof]\033[0m")


    # vérifier si le fichier est vide
    if os.stat(DB).st_size == 0:
        print("\033[95merreur: aucun utilisateur n'existe\033[0m")
        ConnectUserForm(current_mode)

    # saisie du nom d'utilisateur
    while True:
        print("'r': retour")
        print("nom d'utilisateur: ", end="")
        username = input().lower()
        # had an error here once, not sure why
        if username == "r":
            ConnectUserForm(current_mode)
        elif not VerifyUserExistance(username):
            print("erreur: ce nom d'utilisateur n'existe pas")
        elif VerifyUserStatus(username) != current_mode:
            if current_mode == "e":
                print("erreur: ce nom d'utilisateur n'est pas un élève")
                print("voulez-vous vous connecter en tant que prof?", end=" ")
                ActionForm({"o": ("Oui", lambda: SetMode("p")), "n": ("Non", lambda: ConnectUserForm(current_mode))})
            elif current_mode == "p":
                print("erreur: ce nom d'utilisateur n'est pas un prof")
                print("voulez-vous vous connecter en tant qu'élève?", end=" ")
                ActionForm({"o": ("Oui", lambda: SetMode("e")), "n": ("Non", lambda: ConnectUserForm(current_mode))})


        else:
            break

    # saisie du mot de passe, problème ici quelque part
    while True:
        action = None

        print("mot de passe: ", end="")
        this_password = Password()
        if VerifyPassword(username, this_password[0]):
            break
        else:
            print("\033[95merreur: mot de passe incorrect\033[0m")
            ActionForm({"r": ("Réessayer", lambda: None), "m": ("Menu principal", lambda: ConnectUserForm(current_mode))})

    if current_mode == "e":
        print(f"\033[92mconnecté en tant qu'élève '{username}'\033[0m")
    elif current_mode == "p":
        print(f"\033[92mconnecté en tant que prof '{username}'\033[0m")
        MenuProf()


def SignupForm(asmode):
    """Fonction qui permet de créer un compte en saisissant un nom d'utilisateur et un mot de passe et en le confirmant."""
    global current_mode
    if asmode == "e":
        SetMode("e")
        print("\033[93m[créer compte élève]\033[0m")
    elif asmode == "p":
        SetMode("p")
        print("\033[94m[créer compte prof]\033[0m")

    # procédure de création de compte

    # saisie du nom d'utilisateur
    while True:
        # print("\033[2mdebug: this is the while loop for username\033[0m")
        print("'r': retour")
        print("nom d'utilisateur: ", end="")
        username = input().lower()
        if username == "r":
            ConnectUserForm(current_mode)
        elif len(username) < 4:
            print("\033[95merreur: le nom d'utilisateur doit faire au moins 4 caractères\033[0m")
        elif VerifyUserExistance(username):
            print("\033[95merreur: ce nom d'utilisateur existe déjà\033[0m")
            ConnectUserForm(current_mode)
        else:
            break

    # saisie du mot de passe
    while True:
        # print("\033[2mdebug: this is the while loop for password\033[0m")
        new_password = None
        new_password_length = None
        action = None

        while True:
            # demander le mot de passe tant qu'il ne correspond pas aux critères
            print("mot de passe: ", end="")
            new_password = Password()
            if new_password[1] < 4:
                print("\033[95merreur: le mot de passe doit faire au moins 4 caractères\033[0m")
            else:
                break

        while True:
            # print("\033[2mdebug: this is the while loop for password confirmation\033[0m")
            # demander la confirmation du mot de passe tant qu'il ne correspond pas au mot de passe
            print("confirmer mot de passe: ", end="")
            new_password_confirm = Password()
            if new_password_confirm != new_password:
                print("\033[95mles mots de passe ne correspondent pas!\033[0m")
                while True:
                    print(
                        "('r': réessayer, 'd': redéfinir, 'm': menu principal): ",
                        end="",
                    )
                    action = input().lower()

                    if action == "r" or action == "d" or action == "m":
                        break

                if action == "r":
                    # rester dans la boucle si l'utilisateur veut réessayer
                    continue
                elif action == "d":
                    # sortir de la boucle si l'utilisateur veut redéfinir le mot de passe
                    break
                elif action == "m":
                    # retourner au menu principal si l'utilisateur veut retourner au menu principal
                    ConnectUserForm(current_mode)
            else:
                # Les mots de passe correspondent, sortir de la boucle de confirmation
                break

        if action == "d":
            # rester si l'utilisateur veut redéfinir le mot de passe
            continue
        else:
            # sortir si aucune action n'a été prise et donc les mots de passe correspondent
            break
    
    print("\033[2mdebug: this is after the while loop for password confirmation, sending request to create new user\033[0m")
    CreateNewUser(username, new_password[0], current_mode)


def main():
    """Fonction principale qui permet de démarrer le programme."""
    global DB, users, current_mode
    # configurer le dossier data
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")):
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))

    # configurer le logger
    LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "gestionexam.log")
    logging.basicConfig(filename=LOG, level=logging.INFO, format="%(asctime)s [info] %(message)s")
    print("\033[2mdebug: started logging\033[0m")
    logging.info("program started")

    # Gestion du fichier users.json
    DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "users.json")
    logging.info(f"user database: {DB}")
    # s'assurer que le fichier users.json existe et créer le fichier s'il n'existe pas
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
    
    print("\033c") # nettoyer l'écran
    DefineModeForm() # commencer par le menu qui permet de définir le mode de gestion des examens

if __name__ == "__main__":
    # exécuter le programme si le fichier est exécuté directement.
    main()
