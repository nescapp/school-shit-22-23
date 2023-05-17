# importation des modules
import json
import os
import getpass
import msvcrt
import hashlib

"""
Modules utilisés:
json: pour la gestion du fichier users.json
os: pour la gestion du chemin du fichier users.json
getpass et msvcrt: pour cacher le mot de passe de l'utilisateur lors de la saisie dans la CLI
hashlib: pour hasher le mot de passe de l'utilisateur en SHA256
"""


def tempResetUsers():
    """Fonction qui permet de réinitialiser le fichier users.json. Cette fonction est temporaire et sera supprimée dans la version finale."""
    open(DB, "w").close()
    CreateNewUser("eleve", hashlib.sha256('eleve'.encode()).hexdigest(), "e", False)
    CreateNewUser("prof", hashlib.sha256('prof'.encode()).hexdigest(), "p", False)
    print("\033[92mUtilisateurs réinitialisés avec succès.\033[0m")
    DefineMode()


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
        DefineMode()  # retourner au menu principal
    else:
        print("aucun utilisateur")
        DefineMode()  # retourner au menu principal


def Password():
    """Fonction qui permet de cacher le mot de passe de l'utilisateur lors de la saisie dans la CLI et de le hasher en SHA256"""
    password = ""
    length = 0
    print("\033[2m", end="")
    while True:
        last_char = msvcrt.getch().decode("utf-8") # récupérer le dernier caractère
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
            print("erreur: Ce nom d'utilisateur existe déjà.")
            return

    users[username] = {"password": hash, "type": type}

    with open(DB, "w") as file:
        json.dump(users, file, indent=4)

    if verbose:
        if type == "e":
            print(f"compte \033[93m(élève) '{username}'\033[0m créé avec succès")
        elif type == "p":
            print(f"compte \033[94m(prof) '{username}'\033[0m créé avec succès")


def ConnectUser(mode):
    """Fonction qui permet de connecter un utilisateur soit par un login soit par un signup."""
    if mode == "e":
        print(
            "connecter utilisateur \033[93mélève\033[0m ('l': login, 's': signup, 'r': retour, 'q': quitter): ",
            end="",
        )
    elif mode == "p":
        print(
            "connecter utilisateur \033[94mprof\033[0m ('l': login, 's': signup, 'r': retour, 'q': quitter): ",
            end="",
        )

    action = input().lower()  # récupérer l'action de l'utilisateur

    if action == "l":
        LoginForm(mode)
    elif action == "s":
        SignupForm(mode)
    elif action == "r":
        mode = DefineMode()
    elif action == "q":
        # nettoyer l'écran et quitter le programme
        print("\033c")
        exit()
    else:
        # action inconnue, tentative de connexion à nouveau
        print("\033c")
        print("action inconnue")
        ConnectUser(mode)


def DefineMode():
    """Formulaire qui permet de définir le mode de gestion des examens."""
    print(
        "choisiser mode de gestion des examens ('e': élève, 'p': prof, 'x':reset, 'l':liste, 'q': quitter): ",
        end="",
    )
    action = input().lower()  # récupérer l'action de l'utilisateur

    if action == "e":
        print("\033[93m[mode élève]\033[0m")
        ConnectUser(action)
    elif action == "p":
        print("\033[94m[mode prof]\033[0m")
        ConnectUser(action)
    elif action == "x":
        tempResetUsers()
    elif action == "l":
        UserList()
    elif action == "q":
        # nettoyer l'écran et quitter le programme
        print("\033c")
        exit()
    else:
        # action inconnue, tentative de sélection de mode à nouveau
        DefineMode()


def LoginForm(mode):
    """Formulaire de connexion à un compte."""
    # titre: se connecter à son compte
    if mode == "e":
        print("\033[93m[se connecter à son compte élève]\033[0m")
    elif mode == "p":
        print("\033[94m[se connecter à son compte prof]\033[0m")

    print("'r': retour")

    # vérifier si le fichier est vide
    if os.stat(DB).st_size == 0:
        print("aucun utilisateur n'existe")
        ConnectUser(mode)

    # saisie du nom d'utilisateur
    while True:
        print("nom d'utilisateur: ", end="")
        username = input().lower()
        # had an error here once, not sure why
        if username == "r":
            ConnectUser(mode)
        elif not VerifyUserExistance(username):
            print("erreur: ce nom d'utilisateur n'existe pas")
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
            while True:
                print("('r': réessayer, 'm': menu principal): ", end="")
                action = input().lower()

                if action == "r" or action == "m":
                    break

        if action == "r":
            # rester dans la boucle si l'utilisateur veut réessayer
            continue
        elif action == "m":
            # retourner au menu principal si l'utilisateur veut retourner au menu principal
            ConnectUser(mode)
        else:
            # peut être inutile
            break


def SignupForm(mode):
    """Fonction qui permet de créer un compte en saisissant un nom d'utilisateur et un mot de passe et en le confirmant."""
    # titre: créer un compte
    if mode == "e":
        print("\033[93m[créer compte élève]\033[0m")
    elif mode == "p":
        print("\033[94m[créer compte prof]\033[0m")

    print("'r': retour")
    # procédure de création de compte

    # saisie du nom d'utilisateur
    while True:
        print("nom d'utilisateur: ", end="")
        username = input().lower()
        if username == "r":
            ConnectUser(mode)
        elif len(username) < 4:
            print("erreur: le nom d'utilisateur doit faire au moins 4 caractères")
        elif VerifyUserExistance(username):
            print("erreur: ce nom d'utilisateur existe déjà")
            ConnectUser(mode)
        else:
            break

    # saisie du mot de passe
    while True:
        new_password = None
        new_password_length = None
        action = None

        while True:
            # demander le mot de passe tant qu'il ne correspond pas aux critères
            print("mot de passe: ", end="")
            new_password = Password()
            if new_password[1] < 4:
                print("erreur: le mot de passe doit faire au moins 4 caractères")
            else:
                break

        while True:
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
                    ConnectUser(mode)
            else:
                # Les mots de passe correspondent, sortir de la boucle de confirmation
                break

        if action == "d":
            # rester si l'utilisateur veut redéfinir le mot de passe
            continue
        else:
            # sortir si aucune action n'a été prise et donc les mots de passe correspondent
            break

    CreateNewUser(username, new_password[0], mode)


def main():
    # nettoyer l'écran
    print("\033c")
    # définir le mode de gestion des examens
    mode = DefineMode()


# Gestion du fichier users.json
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.json")
# s'assurer que le fichier users.json existe et créer le fichier s'il n'existe pas
if not os.path.exists(DB):
    open(DB, "w").close()
else:
    # maintenant que le fichier existe, vérifier s'il est vide
    if os.stat(DB).st_size == 0:
        # si le fichier est vide, créer le dictionnaire
        users = {}
    else:
        # si le fichier n'est pas vide, trier les utilisateurs par type
        with open(DB, "r") as file:
            users = json.load(file)
        users = dict(
            sorted(users.items(), key=lambda item: item[1]["type"], reverse=True)
        )
        with open(DB, "w") as file:
            json.dump(users, file, indent=4)

if __name__ == "__main__":
    # exécuter le programme si le fichier est exécuté directement.
    main()
